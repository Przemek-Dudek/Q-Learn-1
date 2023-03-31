# Q-Learn-1-
Pierwsze podejście do Q-learningu.

☒☐☐☐☐☐☑

Zadaniem programu jest nauczenie się przechodzić od pozycji startowej ☒ (stan 0) do pozycji docelowej ☑ (stan 6)
Możliwych jest 7 stanów (od 0-6) oraz 2 kierunki poruszania (L, P). W przypadku ruchu w lewo na pozycji startowej (stan 0), pozycja nie zmienia się.

Algorytm decyduje o ruchu za pomocą funkcji next_move().
Następny ruch wyliczany jest na 2 sposoby zależne od wartości EPSILON (Im większa wartość epsilon, tym większa szansa na wylosowanie ruchu)
W przeciwnym przypadku wybierany jest kierunek o większej wadze.

Algorytm "nagradzany jest", po osiągnięciu stanu 6 wartością 1 oraz liczone są wagi poszczególnych ruchów w stanie z którego dostaliśmy się do następnego stanu.
Opisuje to wzór:
Q(st, at) = Q(st, at) + α[rt+1 + γ*maxaQ(st+1, a) - Q(st, at)]
W moim programi jest to zaimplementowane w funkcji: calculate_reward()

Wraz z osiągnięciem stanu 6 przejście funkcji one_pass() kończy się.
