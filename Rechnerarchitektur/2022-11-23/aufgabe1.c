char *answer = "Result =";
int i1 = 5;

int main() {
  int t0 = i1;
  int t1 = 1;
  int t2 = 0;
  while (t0 != 0) {
    t2 = t2 + t1;
    t0 = t0 - 1;
    t1 <<= 1;
  }
  put(answer);
  printf("%d", t2);
  exit(0);
}