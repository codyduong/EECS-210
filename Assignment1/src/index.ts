/** 
 * Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
 * KUID: 3050266
 * Date: 2022-09-1
 * Lab: Assignment 1
 * Purpose: Generates truth tables for assignment one
*/

// Parameters to feed into generateColumn with varying length
const GENERATE_P_GENERIC = (n: number) =>
  [
    (_v: boolean, i: number): boolean => {
      return i % 2 != 0;
    },
    Array(n).fill(false),
  ] as const;
// Parameters to feed into generateColumn with length dependent on third parameter
const GENERATE_Q = [
  (_v: boolean, i: number): boolean => {
    return i % 4 >= 2;
  },
] as const;

/**
 * Generates a column with l length and f function, this is a kind of unidiomatic .map... w/e
 * @param f A function which takes in an index (row) and generates a value based on the index
 * @param l column length
 * @param m an optional map to iterate over
 * @returns column
 */
function generateColumn(
  f: (value: boolean, index: number, array: boolean[]) => boolean,
  m: boolean[]
): boolean[] {
  return m.map(f);
}

// P row of 4 elements
const P = generateColumn(...GENERATE_P_GENERIC(4));
// QP is a table of Q and P with 4 elements
const QP = {
  Q: generateColumn(...([...GENERATE_Q, P] as const)),
  P,
};

type Table = Record<string, boolean[]>;

/**
 * Formats and prints objects in a truth table form that is easily readable
 * @param o table to pretty print
 * @param title title to prepend table with
 */
function prettyPrintTruthTable(
  o: Record<string, boolean[]>,
  title: string
): void {
  const values = Object.values(o);
  const keys = Object.keys(o);
  const header = keys.map((v) => v.padEnd(16)).join('');
  console.log(title);
  console.log(header);
  for (
    let i = 0;
    // reduce and find the largest value so we don't cut off columns
    i < values.reduce((p, c) => (p > c.length ? p : c.length), 0);
    i++
  ) {
    let row = '';
    for (let j = 0; j < keys.length; j++) {
      row += `${values[j][i]}`.padEnd(16);
    }
    console.log(row);
  }
  console.log();
}

function dmorgan1(): void {
  const table: Table = Object.assign({}, QP);
  table['¬P'] = generateColumn((v) => !v, table['P']);
  table['¬Q'] = generateColumn((v) => !v, table['Q']);
  // eslint-disable-next-line prettier/prettier
  table['¬P ∨ ¬Q'] = generateColumn((v, i) => v || table['¬Q'][i],table['¬P']);
  table['P ∧ Q'] = generateColumn((v, i) => v && table['Q'][i], table['P']);
  table['¬(¬P ∨ ¬Q)'] = generateColumn((v) => !v, table['¬P ∨ ¬Q']);

  prettyPrintTruthTable(table, 'De Morgan’s First Law');
}

function dmorgan2(): void {
  const table: Table = Object.assign({}, QP);
  table['¬P'] = generateColumn((v) => !v, table['P']);
  table['¬Q'] = generateColumn((v) => !v, table['Q']);
  // eslint-disable-next-line prettier/prettier
  table['¬P ∧ ¬Q'] = generateColumn((v, i) => v && table['¬Q'][i],table['¬P']);
  table['P ∨ Q'] = generateColumn((v, i) => v || table['Q'][i], table['P']);
  table['¬(¬P ∧ ¬Q)'] = generateColumn((v) => !v, table['¬P ∧ ¬Q']);

  prettyPrintTruthTable(table, 'De Morgan’s Second Law');
}
// generates a table with P values up to 8 instead of 4
const P_eight = generateColumn(...GENERATE_P_GENERIC(8));
const Q_eight = generateColumn(...([...GENERATE_Q, P_eight] as const));
const RQP = {
  R: generateColumn((_v, i) => i % 8 >= 4, Q_eight),
  Q: Q_eight,
  P: P_eight,
};

function firstassociativelaw(): void {
  const table: Table = Object.assign({}, RQP);
  table['Q ∨ R'] = generateColumn((v, i) => v || table['R'][i], table['Q']);
  table['P ∨ Q'] = generateColumn((v, i) => v || table['P'][i], table['Q']);
  // eslint-disable-next-line prettier/prettier
  table['P ∨ (Q ∨ R)'] = generateColumn((v, i) => v || table['P'][i], table['Q ∨ R']);
  // eslint-disable-next-line prettier/prettier
  table['(P ∨ Q) ∨ R)'] = generateColumn((v, i) => v || table['R'][i], table['P ∨ Q']);

  prettyPrintTruthTable(table, 'First Associative Law');
}

function secondassociativelaw(): void {
  const table: Table = Object.assign({}, RQP);
  table['Q ∧ R'] = generateColumn((v, i) => v && table['R'][i], table['Q']);
  table['P ∧ Q'] = generateColumn((v, i) => v && table['P'][i], table['Q']);
  // eslint-disable-next-line prettier/prettier
  table['P ∧ (Q ∧ R)'] = generateColumn((v, i) => v && table['P'][i], table['Q ∧ R']);
  // eslint-disable-next-line prettier/prettier
  table['(P ∧ Q) ∧ R)'] = generateColumn((v, i) => v && table['R'][i], table['P ∧ Q']);

  prettyPrintTruthTable(table, 'Second Associative Law');
}

// 5. [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r ≡ T
function problem5(): void {
  const table: Table = Object.assign({}, RQP);
  table['P ∨ Q'] = generateColumn((v, i) => v || table['P'][i], table['Q']);
  // !p || q  https://stackoverflow.com/questions/19894893/javascript-material-conditional
  table['P → R'] = generateColumn((v, i) => !v || table['R'][i], table['P']);
  table['Q → R'] = generateColumn((v, i) => !v || table['R'][i], table['Q']);
  // eslint-disable-next-line prettier/prettier
  table["[...]"] = generateColumn((v, i) => v && table['P ∨ Q'][i] && table['P → R'][i], table['Q → R']);
  // eslint-disable-next-line prettier/prettier
  table["[] → R"] = generateColumn((v, i) => !v || table['R'][i], table["[...]"]);

  prettyPrintTruthTable(table, '[(p ∨ q) ∧ (p → r) ∧ (q → r)] → r ≡ T');
}

// p ↔ q ≡ (p → q) ∧ (q → p)
function problem6(): void {
  const table: Table = Object.assign({}, QP);
  table['P → Q'] = generateColumn((v, i) => !v || table['Q'][i], table['P']);
  table['Q → P'] = generateColumn((v, i) => !v || table['P'][i], table['Q']);
  // eslint-disable-next-line prettier/prettier
  table['(P→Q)∧(Q→P)'] = generateColumn((v, i) => v && table['Q → P'][i],table['P → Q']);
  // eslint-disable-next-line prettier/prettier
  table['P ↔ Q'] = generateColumn((v, i) => (v && table['P'][i]) || (!v && !table['P'][i]),table['Q']);

  prettyPrintTruthTable(table, 'p ↔ q ≡ (p → q) ∧ (q → p)');
}

dmorgan1();
dmorgan2();
firstassociativelaw();
secondassociativelaw();
problem5();
problem6();
