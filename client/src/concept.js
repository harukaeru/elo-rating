const ratings = {
  A: 1500,
  B: 1500,
  C: 1500,
  D: 1500,
};

const battle = (a: string, b: string) => {
  const w_ab = 1 / (10 ** ((ratings[b] - ratings[a]) / 400) + 1);
  // a win
  ratings[a] = ratings[a] + 32 * (1 - w_ab);
  ratings[b] = ratings[b] + 32 * (0 - w_ab);
};

battle('A', 'B');
battle('A', 'C');
battle('C', 'D');
battle('B', 'D');
battle('A', 'D');
battle('B', 'C');

console.log('ratings', ratings);