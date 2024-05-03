use std::collections::{BTreeMap, HashSet};

use ordered_float::OrderedFloat;

#[derive(Clone, Debug, PartialEq, Eq, Hash, PartialOrd)]
struct Point2D {
    x: OrderedFloat<f64>,
    y: OrderedFloat<f64>,
}

struct ClosestPair2D {
    strip_points: BTreeMap<OrderedFloat<f64>, HashSet<Point2D>>,
    current_closest_pair: Option<(Point2D, Point2D)>,
    current_closest_distance: f64,
}

impl ClosestPair2D {
    fn new(points: Vec<Point2D>) -> ClosestPair2D {
        ClosestPair2D {
            strip_points: BTreeMap::new(),
            current_closest_pair: None,
            current_closest_distance: std::f64::INFINITY,
        }
    }

    fn closest_pair(&mut self, points: Vec<Point2D>) -> (Point2D, Point2D) {
        // sort points by x-coordinate
        let mut sorted_points = points.clone();
        sorted_points.sort_by(|a, b| a.x.partial_cmp(&b.x).unwrap());

        let mut left = 0;
        let mut right = 0;
        
        while right < sorted_points.len() {
            let right_point = &sorted_points[right];

            // first, remove old points from strip_points
            while (right_point.x - sorted_points[left].x) > OrderedFloat(self.current_closest_distance) {
                let left_point = &sorted_points[left];
                let left_point_slot = self.strip_points.get_mut(&left_point.y);
                if let Some(left_point_slot) = left_point_slot {
                    if left_point_slot.remove(&left_point) {
                        left += 1;
                    }
                    if left_point_slot.is_empty() {
                        self.strip_points.remove(&left_point.y);
                    }
                }
            }

            // second, check existing points for distance
            
            // first, range query
            let mut iter = self.strip_points.range((right_point.y - self.current_closest_distance - 1.)..=(right_point.y + self.current_closest_distance + 1.));
            
            // second, check distance
            while let Some((_, points)) = iter.next() {
                for point in points {
                    let distance = (point.x - right_point.x).powi(2) + (point.y - right_point.y).powi(2);
                    if distance < self.current_closest_distance.powi(2) {
                        self.current_closest_distance = distance.sqrt();
                        self.current_closest_pair = Some((point.clone(), right_point.clone()));
                    }
                }
            }

            // third, insert right_point into strip_points
            let right_point_slot = self.strip_points.entry(right_point.y).or_insert(HashSet::new());
            right_point_slot.insert(right_point.clone());
            
            println!("left: {}, right: {}, current_closest_distance: {}, current_closest_pair: {:?}", left, right, self.current_closest_distance, self.current_closest_pair);
            println!("strip_points: {:?}", self.strip_points);
            println!("points: {:?}", points);

            right += 1;
        }

        self.current_closest_pair.clone().unwrap()
    }

}


fn main() {
}


#[cfg(test)]
mod tests {
    use proptest::{strategy::Strategy, test_runner::{Config, TestRunner}};
    use rand::prelude::SliceRandom;


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

    fn squared_distance(p1: &Point2D, p2: &Point2D) -> f64 {
        (p1.x - p2.x).powi(2) + (p1.y - p2.y).powi(2)
    }
    
    fn arb_point() -> impl Strategy<Value = Point2D> {
        (0..1000u32, 0..1000u32).prop_map(|(x, y)| Point2D {
            x: OrderedFloat(x as f64),
            y: OrderedFloat(y as f64),
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
    fn test_closest_pair_2d_a() {
        let mut runner = TestRunner::new(Config {
            verbose: 0,
            cases: 10000,
            test_name: Some("test closest pair 2d a"),
            .. Config::default()
        });
        runner
            .run(&(arb_points()), |points| {
                let (p1, p2) = ClosestPair2D::new(points.clone()).closest_pair(points.clone());
                let (p3, p4) = naive_closest_pair_2d(points.clone());
                // assert_eq!(p1, p3);
                // assert_eq!(p2, p4);
                assert_eq!(squared_distance(&p1, &p2), squared_distance(&p3, &p4));
                Ok(())
            })
            .unwrap();
    }
}
