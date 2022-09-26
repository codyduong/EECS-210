use ndarray::{Array2, ArrayBase, Dim, OwnedRepr};
use std::{
    collections::{hash_map::RandomState, HashSet},
    ops::Mul,
};

fn main() {
    problem1();
    problem2();
    problem3();
    problem4();
}

type Point = (u8, u8);

/// Pretty prints a point out to std.out
///
/// # Arguments
///
/// * `point` - A point tuple of (i8, i8)
fn print_point(point: &Point) {
    let (x, y) = point;
    println!("({x}, {y})");
}

/// Solves problem 1
/// 1. For the relations:
/// R1 = {(1,1), (2,2), (3,3)} and R2 = {(1,1), (1,2), (1,3), (1,4)}
/// perform the following set operations and display the results:
/// a) R1 ∪ R2
/// b) R1 ∩ R2
/// c) R1 − R2
/// d) R2 − R1
fn problem1() {
    let r1: HashSet<Point> = HashSet::from([(1, 1), (2, 2), (3, 3)]);
    let r2: HashSet<Point> = HashSet::from([(1, 1), (1, 2), (1, 3), (1, 4)]);

    // a) R1 ∪ R2
    println!("1a) R1 ∪ R2");
    for point in r1.union(&r2) {
        print_point(&point);
    }

    // b) R1 ∩ R2
    println!("\n1b) R1 ∩ R2");
    for point in r1.intersection(&r2) {
        print_point(&point);
    }

    // c) R1 − R2
    println!("\n1c) R1 − R2");
    for point in r1.difference(&r2) {
        print_point(&point);
    }

    // c) R1 − R2
    println!("\n1d) R2 − R1");
    for point in r2.difference(&r1) {
        print_point(&point);
    }
}

/// Creates a square matrix from a set
///
/// # Arguments
///
/// * `set` - A HashSet of Points
/// * `size` - Matrix size
fn create_square_matrix_unsigned(
    a: &HashSet<Point>,
    size: &u8,
) -> ArrayBase<OwnedRepr<u8>, Dim<[usize; 2]>> {
    let mut matrix: Array2<u8> = Array2::zeros((usize::from(*size), usize::from(*size)));
    for point in a {
        let (x, y) = point;
        matrix[[usize::from(*x - 1), usize::from(*y - 1)]] = 1
    }
    return matrix;
}

/// Solves problem 2
/// Display S ◦ R, where:
/// R is the relation from
///     A = {1, 2, 3} to B = {1, 2, 3, 4} with  
///     R = {(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)}
/// S is the relation from
///     B = {1, 2, 3, 4} to C = {0, 1, 2} with
///     S = {(1, 0), (2, 0), (3, 1), (3, 2), (4, 1)}
fn problem2() {
    let r: HashSet<Point> = HashSet::from([(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)]);
    //  C = {0, 1, 2} -> {1, 2, 3}
    // C + 1 -> to 1 indice
    let s: HashSet<Point> = HashSet::from([(1, 1), (2, 1), (3, 2), (3, 3), (4, 2)]);

    let r_matrix = create_square_matrix_unsigned(&r, &4);
    let s_matrix = create_square_matrix_unsigned(&s, &4);
    // println!("{}", r_matrix);
    // println!("{}", s_matrix);
    println!("\n2. Display S ◦ R...");
    println!("{}", r_matrix.dot(&s_matrix));
}

/// Solves problem 3
/// For R = {(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)}, show R2.
fn problem3() {
    let r: HashSet<Point> = HashSet::from([(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)]);

    let r_matrix = create_square_matrix_unsigned(&r, &4);
    // println!("{}", r_matrix);
    println!("\n3. For R = {{(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)}}, show R2.");
    println!("{}", r_matrix.dot(&r_matrix));
}

/// Solves problem 4
/// For the relation R = {(x, y) | x + y = 0} on the set {-10, ..., -1, 0, 1, ..., 10}:
/// a) Show R as a set of ordered pairs.
/// b) Show whether R is reflexive or not.
/// c) Show whether R is symmetric or not.
/// d) Show whether R is antisymmetric or not.
/// e) Show whether R is transitive or not.
fn problem4() {
    let x: [i8; 21] = core::array::from_fn(|x| x as i8 - 10);
    let y = x;

    let pairs = x
        .iter()
        .filter(|x| y.contains(&x.mul(-1)))
        .map(|x| (x, x.mul(-1)));
    let r: HashSet<(&i8, i8), RandomState> = HashSet::from_iter(pairs);

    // a) Show R as a set of ordered pairs.
    // order is random based on hasher
    println!("\n4a) Show R as a set of ordered pairs.");
    for point in r.clone() {
        let (x, y) = point;
        println!("({x}, {y})");
    }

    let mut r_matrix: Array2<i8> = Array2::zeros((21, 21));
    for point in r {
        let (x, y) = point;
        let x_shift = x+10;
        let y_shift = y+10;
        r_matrix[[usize::from(x_shift as i8 as u8), usize::from(y_shift as i8 as u8)]] = 1
    }
    println!("\n4b) Show whether R is reflexive or not.");
    println!("{}", r_matrix);
    println!("{}", r_matrix.diag());
}
