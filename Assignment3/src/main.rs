use ndarray::{Array2, ArrayBase, Dim, OwnedRepr};
use std::cmp;
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

type PointU8 = (u8, u8);
type PointI8 = (i8, i8);

/// Macro hack to assert tuples, since I have no clue how to use Rust idiomatically
/// https://stackoverflow.com/a/70719105/17954209
macro_rules! tuple_as {
    ($t: expr, $ty: ident) => {{
        let (a, b) = $t;
        let a = a as $ty;
        let b = b as $ty;
        (a, b)
    }};
    ($t: expr, ($ty: ident)) => {{
        let (a, b) = $t;
        let a = a as $ty;
        let b = b as $ty;
        (a, b)
    }};
    ($t: expr, ($($ty: ident),*)) => {{
        let ($($ty,)*) = $t;
        ($($ty as $ty,)*)
    }};
}

/// Pretty prints a point out to std.out
///
/// As an aside, if I knew more about how generics worked in Rust maybe I could get this to work w/o macro hack
///
/// # Arguments
///
/// * `point` - A point tuple of (i8, i8)
fn print_point(point: &PointI8) {
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
    let r1: HashSet<PointU8> = HashSet::from([(1, 1), (2, 2), (3, 3)]);
    let r2: HashSet<PointU8> = HashSet::from([(1, 1), (1, 2), (1, 3), (1, 4)]);

    // a) R1 ∪ R2
    println!("1a) R1 ∪ R2");
    for point in r1.union(&r2) {
        print_point(&tuple_as!(*point, (i8)));
    }

    // b) R1 ∩ R2
    println!("\n1b) R1 ∩ R2");
    for point in r1.intersection(&r2) {
        print_point(&tuple_as!(*point, (i8)));
    }

    // c) R1 − R2
    println!("\n1c) R1 − R2");
    for point in r1.difference(&r2) {
        print_point(&tuple_as!(*point, (i8)));
    }

    // c) R1 − R2
    println!("\n1d) R2 − R1");
    for point in r2.difference(&r1) {
        print_point(&tuple_as!(*point, (i8)));
    }
}

/// Creates a square matrix from a set
///
/// Ndarray requires matrix values be all >= 0, assume all points are bound >= (1, 1), thus subract to 0 to get 0 indices
///
/// # Arguments
///
/// * `set` - A HashSet of Points
/// * `size` - Matrix size
fn create_square_matrix_unsigned(
    a: &HashSet<PointU8>,
) -> ArrayBase<OwnedRepr<u8>, Dim<[usize; 2]>> {
    let size_tuple_max = a.clone().into_iter().max().unwrap();
    let size_tuple_min = a.clone().into_iter().min().unwrap();
    let size = (cmp::max(
        size_tuple_max.0 as i8 - size_tuple_min.0 as i8,
        size_tuple_max.1 as i8 - size_tuple_min.1 as i8,
    ) + 1) as u8;
    let mut matrix: Array2<u8> = Array2::zeros((usize::from(size), usize::from(size)));
    for point in a {
        let (x, y) = point;
        matrix[[usize::from(*x - 1), usize::from(*y - 1)]] = 1
    }
    if !matrix.is_square() {
        panic!()
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
    let r: HashSet<PointU8> = HashSet::from([(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)]);
    //  C = {0, 1, 2} -> {1, 2, 3}
    // C + 1 -> to 1 indice
    let s: HashSet<PointU8> = HashSet::from([(1, 1), (2, 1), (3, 2), (3, 3), (4, 2)]);

    let r_matrix = create_square_matrix_unsigned(&r);
    let s_matrix = create_square_matrix_unsigned(&s);

    println!("\n2. Display S ◦ R...");
    println!("{}", r_matrix.dot(&s_matrix));
}

/// Solves problem 3
/// For R = {(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)}, show R^2.
fn problem3() {
    let r: HashSet<PointU8> = HashSet::from([(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)]);

    let r_matrix = create_square_matrix_unsigned(&r);
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
    // Build an array from -10 to 10 inclusive
    let x: [i8; 21] = core::array::from_fn(|x| x as i8 - 10);
    let y = x;

    // Generate the ordered pairs that obey the predicate function
    let pairs = x
        .iter()
        .filter(|x| y.contains(&x.mul(-1)))
        .map(|x| (*x, x.mul(-1)));
    let r: HashSet<(i8, i8), RandomState> = HashSet::from_iter(pairs.clone());

    // a) Show R as a set of ordered pairs.
    // order is random based on hasher
    println!("\n4a) Show R as a set of ordered pairs.");
    for point in r.clone() {
        print_point(&tuple_as!(point, (i8)))
    }

    // Creates a matrix for 4b-4e
    // Offsetting by minimum value since ndarray requires all dims to be unsigned
    let offset_value = pairs.clone().into_iter().min().unwrap().0 * -1 + 1;
    // Map the ordered values onto the new offset pairs
    let offset_pairs =
        pairs.map(|pair| tuple_as!((pair.0 + offset_value, pair.1 + offset_value), u8));
    // Create the offset set
    let r_offset = HashSet::from_iter(offset_pairs);
    // Actually create the matrix
    let r_matrix = create_square_matrix_unsigned(&r_offset);

    // b) Show whether R is reflexive or not.
    let r_diagonal = r_matrix.diag();
    println!(
        "\n4b) Show whether R is reflexive or not. {}",
        r_diagonal.into_iter().all(|v| v == &1)
    );
    println!("Diagonal: {}", r_diagonal);

    // c) Show whether R is symmetric or not.
    let max_size = r_matrix.columns().into_iter().len();
    let mut symmetric = true;
    let mut symmetric_antiproof: (u8, u8) = (0, 0);
    // We only have to check above the diagonal, otherwise it is redundant
    for left_bound in 0..max_size {
        for right_bound in left_bound..max_size {
            // prevent unnecessary calculations
            if symmetric == false {
                continue;
            }
            if r_matrix[[left_bound, right_bound]] != r_matrix[[right_bound, left_bound]] {
                symmetric = false;
                symmetric_antiproof = (
                    left_bound.try_into().unwrap(),
                    right_bound.try_into().unwrap(),
                );
            }
        }
    }
    println!("\n4c) Show whether R is reflexive or not: {}", symmetric);
    if symmetric {
        println!("No point disproving symmetry");
    } else {
        println!(
            "Disproven by point: ({0}, {1}) ≠ ({2}, {3})",
            // convert back to original ordered pairs (+1 is necessary since zero-indexed)
            symmetric_antiproof.0 as i8 - offset_value + 1,
            symmetric_antiproof.1 as i8 - offset_value + 1,
            symmetric_antiproof.1 as i8 - offset_value + 1,
            symmetric_antiproof.0 as i8 - offset_value + 1
        );
    }

    // d) Show whether R is antisymmetric or not.
    // We only have to check above the diagonal, otherwise it is redundant
    let mut antisymmetric = true;
    let mut antisymmetric_antiproof: (i8, i8) = (0, 0);
    for left_bound in 0..max_size {
        for right_bound in left_bound..max_size {
            // prevent unnecessary calculations
            if antisymmetric == false {
                continue;
            }
            if r_matrix[[left_bound, right_bound]] == r_matrix[[right_bound, left_bound]] {
                antisymmetric = false;
                antisymmetric_antiproof = (
                    left_bound.try_into().unwrap(),
                    right_bound.try_into().unwrap(),
                );
            }
        }
    }
    println!(
        "\n4d) Show whether R is antisymmetric or not: {}",
        antisymmetric
    );
    if antisymmetric {
        println!("No point disproving antisymmetry");
    } else {
        println!(
            "Disproven by point: ({0}, {1}) = ({2}, {3})",
            antisymmetric_antiproof.0 as i8 - offset_value + 1,
            antisymmetric_antiproof.1 as i8 - offset_value + 1,
            antisymmetric_antiproof.1 as i8 - offset_value + 1,
            antisymmetric_antiproof.0 as i8 - offset_value + 1
        );
    }

    // e) Show whether R is transitive or not.
    // I'm sure you only need to check one diagonal rather than the whole matrix...
    // Something something could cut calculation time in half in worst-case... w/e
    let mut transitive = true;
    for i in 0..max_size {
        for j in 0..max_size {
            for k in 0..max_size {
                // prevent unnecessary calculations
                if transitive == false {
                    continue;
                }
                if r_matrix[[i, j]] == 1 && r_matrix[[j, k]] == 1 {
                    if r_matrix[[i, k]] != 1 {
                        transitive = false
                    }
                }
            }
        }
    }
}
