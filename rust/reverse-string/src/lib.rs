pub fn reverse(input: &str) -> String {
  // graphemes are user-perceived characters
  let reversed: String = input.chars().rev().collect::<String>();
  return reversed;
}
