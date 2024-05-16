use std::collections::{HashMap, HashSet};
use std::fmt::Debug;
use std::hash::Hash;

pub struct DenseDFA<
    Character: Debug + Copy + Eq + Hash,
    StateID: Debug + Clone + Eq + Hash + Default,
> {
    lookup_table: HashMap<(StateID, Character), StateID>,
    accepting_states: HashMap<StateID, bool>,
    current_state: Option<StateID>,
}

impl<Character: Debug + Copy + Eq + Hash, StateID: Debug + Clone + Eq + Hash + Default>
    DenseDFA<Character, StateID>
{
    pub fn new() -> DenseDFA<Character, StateID> {
        DenseDFA {
            lookup_table: HashMap::new(),
            accepting_states: HashMap::new(),
            current_state: Some(Default::default()),
        }
    }

    pub fn add_transition(&mut self, from: StateID, to: StateID, character: Character) {
        self.lookup_table.insert((from, character), to);
    }

    pub fn add_accepting_state(&mut self, state: StateID) {
        self.accepting_states.insert(state, true);
    }

    pub fn reset(&mut self) {
        self.current_state = Some(Default::default());
    }

    pub fn step(&mut self, character: Character) -> Option<StateID> {
        let current_state = self.current_state.clone()?;
        let next_state = self.lookup_table.get(&(current_state, character)).cloned();
        self.current_state = next_state.clone();
        next_state
    }

    pub fn is_accepting(&self) -> bool {
        self.current_state
            .as_ref()
            .and_then(|state| self.accepting_states.get(state).copied())
            .unwrap_or(false)
    }

    pub fn is_alive(&self) -> bool {
        self.current_state.is_some()
    }

    pub fn is_dead(&self) -> bool {
        self.current_state.is_none()
    }

    pub fn run(&mut self, input: &[Character]) -> bool {
        self.reset();
        for &character in input {
            self.step(character);
        }
        println!("Current state: {:?}", self.current_state);
        self.is_accepting()
    }
}

pub struct DenseNFA<
    Character: Debug + Copy + Eq + Hash,
    StateID: Debug + Clone + Eq + Hash + Default,
> {
    // lookup_table: HashMap<(StateID, Option<Character>), Vec<StateID>>,
    lookup_table: HashMap<StateID, HashMap<Option<Character>, Vec<StateID>>>,
    accepting_states: HashMap<StateID, bool>,
    pub current_states: Vec<StateID>,
}

impl<Character: Debug + Copy + Eq + Hash, StateID: Debug + Clone + Eq + Hash + Default>
    DenseNFA<Character, StateID>
{
    pub fn new() -> DenseNFA<Character, StateID> {
        DenseNFA {
            lookup_table: HashMap::new(),
            accepting_states: HashMap::new(),
            current_states: vec![Default::default()],
        }
    }

    pub fn add_transition(&mut self, from: StateID, to: StateID, character: Option<Character>) {
        // self.lookup_table
        //     .entry((from, character))
        //     .or_insert_with(Vec::new)
        //     .push(to);
        self.lookup_table
            .entry(from)
            .or_insert_with(HashMap::new)
            .entry(character)
            .or_insert_with(Vec::new)
            .push(to);
    }

    pub fn add_accepting_state(&mut self, state: StateID) {
        self.accepting_states.insert(state, true);
    }

    pub fn transition_characters(&self) -> HashSet<Character> {
        // self.lookup_table
        //     .keys()
        //     .filter_map(|(state, character)| character.clone())
        //     .collect()
        self.current_states
            .iter()
            .flat_map(|state| {
                self.lookup_table
                    .get(state)
                    .iter()
                    .flat_map(|map| map.keys().filter_map(|character| character.clone()))
                    .collect::<Vec<_>>()
            })
            .collect()
    }

    pub fn reset(&mut self) {
        self.current_states = vec![Default::default()];
    }

    pub fn epsilon_closure(&self, states: &[StateID]) -> Vec<StateID> {
        let mut closure = HashSet::new();
        let mut stack = states.to_vec();
        while let Some(state) = stack.pop() {
            closure.insert(state.clone());
            // if let Some(next_states) = self.lookup_table.get(&(state.clone(), None)) {
            //     for next_state in next_states {
            //         if !closure.contains(next_state) {
            //             stack.push(next_state.clone());
            //         }
            //     }
            // }
            if let Some(next_states) = self.lookup_table.get(&state) {
                if let Some(next_state) = next_states.get(&None) {
                    for state in next_state {
                        if !closure.contains(state) {
                            stack.push(state.clone());
                        }
                    }
                }
            }
        }
        closure.into_iter().collect()
    }

    pub fn step(&mut self, character: Character) {
        let mut next_states = Vec::new();
        for current_state in &self.current_states {
            // if let Some(states) = self
            //     .lookup_table
            //     .get(&(current_state.clone(), Some(character)))
            // {
            //     next_states.extend_from_slice(states);
            // }
            if let Some(states) = self.lookup_table.get(current_state) {
                if let Some(s) = states.get(&Some(character)) {
                    let mut s = s.clone();
                    next_states.append(&mut s);
                }
            }
        }
        next_states = self.epsilon_closure(next_states.as_slice());
        println!("Next states: {:?}", next_states);
        self.current_states = next_states;
    }

    pub fn is_accepting(&self) -> bool {
        self.current_states
            .iter()
            .any(|state| self.accepting_states.get(state).copied().unwrap_or(false))
    }

    pub fn is_alive(&self) -> bool {
        !self.current_states.is_empty()
    }

    pub fn is_dead(&self) -> bool {
        self.current_states.is_empty()
    }

    pub fn run(&mut self, input: &[Character]) -> bool {
        self.reset();
        for &character in input {
            self.step(character);
        }
        self.is_accepting()
    }
}

pub fn powerset_construction<Character: Debug + Copy + Eq + Hash>(
    nfa: &DenseNFA<Character, usize>,
) -> DenseDFA<Character, Vec<usize>> {
    let mut dfa = DenseDFA::new();
    let mut queue = Vec::new();
    // add start state
    let start_state = nfa.epsilon_closure(&[0]);
    queue.push(start_state.clone());
    dfa.current_state = Some(start_state);
    
    dfa
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_dense_dfa() {
        let mut dfa = DenseDFA::new();
        dfa.add_transition(0, 1, 'a');
        dfa.add_transition(1, 2, 'b');
        dfa.add_transition(2, 3, 'c');
        dfa.add_accepting_state(3);

        assert_eq!(dfa.run(&['a', 'b', 'c']), true);
        assert_eq!(dfa.run(&['a', 'b']), false);
        assert_eq!(dfa.run(&['a', 'b', 'c', 'd']), false);
    }

    #[test]
    fn test_dense_nfa() {
        let mut nfa = DenseNFA::new();
        nfa.add_transition(0, 1, Some('a'));
        nfa.add_transition(1, 2, Some('b'));
        // add 2 to 1 with epsilon
        nfa.add_transition(2, 1, None);
        nfa.add_transition(2, 3, Some('c'));
        nfa.add_accepting_state(3);
        // meaning: ab*c

        assert_eq!(nfa.run(&['a', 'b', 'c']), true);
        assert_eq!(nfa.run(&['a', 'b']), false);
        assert_eq!(nfa.run(&['a', 'b', 'c', 'd']), false);
        assert_eq!(nfa.run(&['a', 'b', 'b', 'c']), true);
    }
}
