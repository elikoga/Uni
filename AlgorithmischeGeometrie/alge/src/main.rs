use rand::prelude::SliceRandom;

#[derive(Clone, Debug, PartialEq, PartialOrd)]
struct Point2D {
    x: f64,
    y: f64,
}

fn distance(p1: Point2D, p2: Point2D) -> f64 {
    ((p1.x - p2.x).powi(2) + (p1.y - p2.y).powi(2)).sqrt()
}

fn squared_distance(p1: &Point2D, p2: &Point2D) -> f64 {
    (p1.x - p2.x).powi(2) + (p1.y - p2.y).powi(2)
}

fn closest_pair_2d(points: Vec<Point2D>) -> (Point2D, Point2D) {
    // sort points by x-coordinate
    let mut sorted_points = points.clone();
    sorted_points.sort_by(|a, b| a.x.partial_cmp(&b.x).unwrap());

    let mut left = 0;
    let mut right = 1;
    let mut best_distance = std::f64::INFINITY;
    let mut best_pair: Option<(Point2D, Point2D)> = None;

    while right < sorted_points.len() {
        // first: move left pointer to the right until the distance between the points is smaller than the best distance
        // find split point by x-coordinate using binary search
        let split_point = sorted_points[left..right]
            .binary_search_by(|point| {
                point
                    .x
                    .partial_cmp(&(sorted_points[right].x - best_distance))
                    .unwrap()
            })
            .unwrap_or_else(|x| x);
        // println!(
        //     "left: {}, right: {}, split_point: {}, best_distance: {}, best_pair: {:?}",
        //     left, right, split_point, best_distance, best_pair
        // );
        left += split_point;

        // check all points left of right pointer, wether they are closer to the right point than the best distance
        for i in left..right {
            if squared_distance(&sorted_points[i], &sorted_points[right]) < best_distance {
                best_distance = squared_distance(&sorted_points[i], &sorted_points[right]);
                best_pair = Some((sorted_points[i].clone(), sorted_points[right].clone()));
            }
        }

        right += 1;
    }

    best_pair.expect("No pair found")
}

fn main() {
    let points = vec![
        Point2D { x: 0.0, y: 0.0 },
        Point2D { x: 1.0, y: 1.0 },
        Point2D { x: 3.0, y: 3.0 },
        Point2D { x: 3.5, y: 3.5 },
        Point2D { x: 5.0, y: 5.0 },
    ];

    let (p1, p2) = closest_pair_2d(points);

    println!("Closest pair: {:?} {:?}", p1, p2);
}

#[cfg(test)]
mod tests {
    use proptest::{strategy::Strategy, test_runner::{Config, TestRunner}};

    use super::*;

    fn naive_closest_pair_2d(points: Vec<Point2D>) -> (Point2D, Point2D) {
        let (p, q) = points
            .iter()
            .flat_map(|p1| points.iter().map(move |p2| (p1, p2)))
            .filter(|(p1, p2)| p1 != p2)
            .min_by(|(p1, p2), (p3, p4)| {
                squared_distance(p1, p2)
                    .partial_cmp(&squared_distance(p3, p4))
                    .unwrap()
            })
            .unwrap();
        (p.clone(), q.clone())
    }

    fn arb_point() -> impl Strategy<Value = Point2D> {
        (0..1000u32, 0..1000u32).prop_map(|(x, y)| Point2D {
            x: x as f64,
            y: y as f64,
        })
    }

    fn arb_points() -> impl Strategy<Value = Vec<Point2D>> {
        proptest::collection::vec(arb_point(), 2..100).prop_map(|points| {
            let mut points = points;
            points.sort_by(|a, b| a.x.partial_cmp(&b.x).unwrap());
            points.sort_by(|a, b| a.y.partial_cmp(&b.y).unwrap());
            points.dedup();
            points.shuffle(&mut rand::thread_rng());
            points
        })
    }

    #[test]
    fn test_closest_pair_2d() {
        let mut runner = TestRunner::new(Config {
            verbose: 0,
            cases: 1000000,
            .. Config::default()
        });
        runner
            .run(&(arb_points()), |points| {
                let (p1, p2) = closest_pair_2d(points.clone());
                let (p3, p4) = naive_closest_pair_2d(points.clone());
                // assert_eq!(p1, p3);
                // assert_eq!(p2, p4);
                assert_eq!(squared_distance(&p1, &p2), squared_distance(&p3, &p4));
                Ok(())
            })
            .unwrap();
    }
}
