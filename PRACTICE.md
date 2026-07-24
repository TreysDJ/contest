# Банк задач

Этот каталог построен под календарь «лето → отборы в октябре–ноябре → финалы в марте–апреле». Он не требует решить все задачи подряд.

## Объём и маршрут

- приоритет A: **180** задач — фундамент и наиболее вероятные темы отборов;
- приоритет B: **77** задач — усиление после прохождения отбора;
- приоритет C: **25** задач — финальный и выборочный продвинутый слой;
- полный каталог: **282** задач Codeforces/ACMP;
- основной маршрут без `H` и `X`: **214** задач;
- LeetCode вынесен отдельно и в эти числа не входит.

Роли: `D` — диагностика; `L` — изучение приёма; `R` — закрепление; `H` — трудная задача; `F` — контрольная задача без подсказок; `X` — задача на сочетание тем. Для быстрого маршрута решать `D/L/R/F`; `H/X` переносить на финальный цикл или брать по слабым местам.

## Правила работы

1. До начала темы решить `D` за ограниченное время. Если идея не найдена, изучить теорию и перейти к `L`.
2. Если задача дала переносимый вывод, записать его одной короткой строкой в [`NOTES.md`](NOTES.md). Для обычного решения без нового вывода заметка не нужна.
3. `F` решать как мини-контест: без подсказок, с полным тестированием и разбором после сдачи.
4. ACMP используется как русскоязычный вход и тренировка реализации; Codeforces — как основная шкала сложности.
5. Рейтинг Codeforces — ориентир, а не строгий порядок: редкая знакомая тема может оказаться легче незнакомой задачи с меньшим рейтингом.

## 1. Оценка сложности, Java и аккуратная реализация

Приоритет **A**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 1](ROADMAP.md#тема-1).

База LeetCode, не входит в лимит: [LC 412 — Fizz Buzz](https://leetcode.com/problems/fizz-buzz/); [LC 66 — Plus One](https://leetcode.com/problems/plus-one/).

|   № | Задача                                                                          | Рейтинг CF | Роль |
| --: | ------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [ACMP 1 — A+B](https://acmp.ru/index.asp?main=task&id_task=1)                   |          — | `D`  |
|   2 | [ACMP 5 — Статистика](https://acmp.ru/index.asp?main=task&id_task=5)            |          — | `L`  |
|   3 | [CF 282A — Bit++](https://codeforces.com/problemset/problem/282/A)              |        800 | `L`  |
|   4 | [CF 158A — Next Round](https://codeforces.com/problemset/problem/158/A)         |        800 | `L`  |
|   5 | [CF 263A — Beautiful Matrix](https://codeforces.com/problemset/problem/263/A)   |        800 | `R`  |
|   6 | [CF 112A — Petya and Strings](https://codeforces.com/problemset/problem/112/A)  |        800 | `R`  |
|   7 | [CF 236A — Boy or Girl](https://codeforces.com/problemset/problem/236/A)        |        800 | `R`  |
|   8 | [CF 339A — Helpful Maths](https://codeforces.com/problemset/problem/339/A)      |        800 | `H`  |
|   9 | [CF 118A — String Task](https://codeforces.com/problemset/problem/118/A)        |       1000 | `F`  |
|  10 | [CF 492B — Vanya and Lanterns](https://codeforces.com/problemset/problem/492/B) |       1200 | `X`  |

## 2. Полный перебор, рекурсия и отсечения

Приоритет **A**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 2](ROADMAP.md#тема-2).

База LeetCode, не входит в лимит: [LC 46 — Permutations](https://leetcode.com/problems/permutations/); [LC 78 — Subsets](https://leetcode.com/problems/subsets/).

|   № | Задача                                                                           | Рейтинг CF | Роль |
| --: | -------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [ACMP 16 — Лесенка](https://acmp.ru/index.asp?main=task&id_task=16)              |          — | `D`  |
|   2 | [ACMP 24 — Вырубка деревьев](https://acmp.ru/index.asp?main=task&id_task=24)     |          — | `L`  |
|   3 | [CF 4A — Watermelon](https://codeforces.com/problemset/problem/4/A)              |        800 | `L`  |
|   4 | [CF 231A — Team](https://codeforces.com/problemset/problem/231/A)                |        800 | `L`  |
|   5 | [CF 546A — Soldier and Bananas](https://codeforces.com/problemset/problem/546/A) |        800 | `R`  |
|   6 | [CF 271A — Beautiful Year](https://codeforces.com/problemset/problem/271/A)      |        800 | `R`  |
|   7 | [CF 122A — Lucky Division](https://codeforces.com/problemset/problem/122/A)      |       1000 | `R`  |
|   8 | [CF 479A — Expression](https://codeforces.com/problemset/problem/479/A)          |       1000 | `H`  |
|   9 | [CF 327A — Flipping Game](https://codeforces.com/problemset/problem/327/A)       |       1200 | `F`  |
|  10 | [CF 279B — Books](https://codeforces.com/problemset/problem/279/B)               |       1400 | `X`  |

## 3. Сортировка, компараторы и сжатие координат

Приоритет **A**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 3](ROADMAP.md#тема-3).

База LeetCode, не входит в лимит: [LC 912 — Sort an Array](https://leetcode.com/problems/sort-an-array/); [LC 56 — Merge Intervals](https://leetcode.com/problems/merge-intervals/).

|   № | Задача                                                                                     | Рейтинг CF | Роль |
| --: | ------------------------------------------------------------------------------------------ | ---------: | :--: |
|   1 | [ACMP 41 — Сортировка подсчетом](https://acmp.ru/index.asp?main=task&id_task=41)           |          — | `D`  |
|   2 | [ACMP 119 — Сортировка времени](https://acmp.ru/index.asp?main=task&id_task=119)           |          — | `L`  |
|   3 | [CF 141A — Amusing Joke](https://codeforces.com/problemset/problem/141/A)                  |        800 | `L`  |
|   4 | [CF 723A — The New Year: Meeting Friends](https://codeforces.com/problemset/problem/723/A) |        800 | `L`  |
|   5 | [CF 1903A — Halloumi Boxes](https://codeforces.com/problemset/problem/1903/A)              |        800 | `R`  |
|   6 | [CF 1399A — Remove Smallest](https://codeforces.com/problemset/problem/1399/A)             |        800 | `R`  |
|   7 | [CF 160A — Twins](https://codeforces.com/problemset/problem/160/A)                         |        900 | `R`  |
|   8 | [CF 405A — Gravity Flip](https://codeforces.com/problemset/problem/405/A)                  |        900 | `H`  |
|   9 | [CF 230A — Dragons](https://codeforces.com/problemset/problem/230/A)                       |       1000 | `F`  |
|  10 | [CF 1201C — Maximum Median](https://codeforces.com/problemset/problem/1201/C)              |       1400 | `X`  |

## 4. Частоты, HashMap/HashSet и множества

Приоритет **A**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 4](ROADMAP.md#тема-4).

База LeetCode, не входит в лимит: [LC 1 — Two Sum](https://leetcode.com/problems/two-sum/); [LC 49 — Group Anagrams](https://leetcode.com/problems/group-anagrams/).

|   № | Задача                                                                                        | Рейтинг CF | Роль |
| --: | --------------------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [ACMP 82 — Пересечение множеств](https://acmp.ru/index.asp?main=task&id_task=82)              |          — | `D`  |
|   2 | [ACMP 816 — Система пересекающихся множеств](https://acmp.ru/index.asp?main=task&id_task=816) |          — | `L`  |
|   3 | [CF 1703B — ICPC Balloons](https://codeforces.com/problemset/problem/1703/B)                  |        800 | `L`  |
|   4 | [CF 1760C — Advantage](https://codeforces.com/problemset/problem/1760/C)                      |        800 | `L`  |
|   5 | [CF 1722C — Word Game](https://codeforces.com/problemset/problem/1722/C)                      |        800 | `R`  |
|   6 | [CF 1955B — Progressive Square](https://codeforces.com/problemset/problem/1955/B)             |       1000 | `R`  |
|   7 | [CF 519B — A and B and Compilation Errors](https://codeforces.com/problemset/problem/519/B)   |       1100 | `R`  |
|   8 | [CF 1213B — Bad Prices](https://codeforces.com/problemset/problem/1213/B)                     |       1100 | `H`  |
|   9 | [CF 1520D — Same Differences](https://codeforces.com/problemset/problem/1520/D)               |       1200 | `F`  |
|  10 | [CF 4C — Registration System](https://codeforces.com/problemset/problem/4/C)                  |       1300 | `X`  |

## 5. Стек, очередь, дек и приоритетная очередь

Приоритет **A**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 5](ROADMAP.md#тема-5).

База LeetCode, не входит в лимит: [LC 20 — Valid Parentheses](https://leetcode.com/problems/valid-parentheses/); [LC 239 — Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/).

|   № | Задача                                                                                       | Рейтинг CF | Роль |
| --: | -------------------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [ACMP 899 — Баланс скобок](https://acmp.ru/index.asp?main=task&id_task=899)                  |          — | `D`  |
|   2 | [ACMP 946 — Полка](https://acmp.ru/index.asp?main=task&id_task=946)                          |          — | `L`  |
|   3 | [CF 450A — Jzzhu and Children](https://codeforces.com/problemset/problem/450/A)              |       1000 | `L`  |
|   4 | [CF 1907B — YetnotherrokenKeoard](https://codeforces.com/problemset/problem/1907/B)          |       1000 | `L`  |
|   5 | [CF 545D — Queue](https://codeforces.com/problemset/problem/545/D)                           |       1300 | `R`  |
|   6 | [CF 26B — Regular Bracket Sequence](https://codeforces.com/problemset/problem/26/B)          |       1400 | `R`  |
|   7 | [CF 343B — Alternating Current](https://codeforces.com/problemset/problem/343/B)             |       1600 | `R`  |
|   8 | [CF 797C — Minimal string](https://codeforces.com/problemset/problem/797/C)                  |       1700 | `H`  |
|   9 | [CF 5C — Longest Regular Bracket Sequence](https://codeforces.com/problemset/problem/5/C)    |       1900 | `F`  |
|  10 | [CF 1092D1 — Great Vova Wall (Version 1)](https://codeforces.com/problemset/problem/1092/D1) |       2200 | `X`  |

## 6. Префиксные суммы, разности, 2D-префиксы и sweep line

Приоритет **A**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 6](ROADMAP.md#тема-6).

База LeetCode, не входит в лимит: [LC 303 — Range Sum Query — Immutable](https://leetcode.com/problems/range-sum-query-immutable/); [LC 304 — Range Sum Query 2D — Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/).

|   № | Задача                                                                                                                  | Рейтинг CF | Роль |
| --: | ----------------------------------------------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [CF 1807D — Odd Queries](https://codeforces.com/problemset/problem/1807/D)                                              |        900 | `D`  |
|   2 | [CF 363B — Fence](https://codeforces.com/problemset/problem/363/B)                                                      |       1100 | `L`  |
|   3 | [CF 313B — Ilya and Queries](https://codeforces.com/problemset/problem/313/B)                                           |       1100 | `L`  |
|   4 | [CF 433B — Kuriyama Mirai's Stones](https://codeforces.com/problemset/problem/433/B)                                    |       1200 | `L`  |
|   5 | [CF 1703F — Yet Another Problem About Pairs Satisfying an Inequality](https://codeforces.com/problemset/problem/1703/F) |       1300 | `R`  |
|   6 | [CF 816B — Karen and Coffee](https://codeforces.com/problemset/problem/816/B)                                           |       1400 | `R`  |
|   7 | [CF 276C — Little Girl and Maximum Sum](https://codeforces.com/problemset/problem/276/C)                                |       1500 | `R`  |
|   8 | [CF 1795C — Tea Tasting](https://codeforces.com/problemset/problem/1795/C)                                              |       1500 | `H`  |
|   9 | [CF 466C — Number of Ways](https://codeforces.com/problemset/problem/466/C)                                             |       1700 | `F`  |
|  10 | [CF 1000C — Covered Points Count](https://codeforces.com/problemset/problem/1000/C)                                     |       1700 | `X`  |

## 7. Два указателя и скользящее окно

Приоритет **A**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 7](ROADMAP.md#тема-7).

База LeetCode, не входит в лимит: [LC 3 — Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/); [LC 11 — Container With Most Water](https://leetcode.com/problems/container-with-most-water/).

|   № | Задача                                                                                            | Рейтинг CF | Роль |
| --: | ------------------------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [ACMP 245 — Сплоченная команда](https://acmp.ru/index.asp?main=task&id_task=245)                  |          — | `D`  |
|   2 | [ACMP 649 — Защищенный пароль](https://acmp.ru/index.asp?main=task&id_task=649)                   |          — | `L`  |
|   3 | [CF 2060C — Game of Mathletes](https://codeforces.com/problemset/problem/2060/C)                  |        900 | `L`  |
|   4 | [CF 1840C — Ski Resort](https://codeforces.com/problemset/problem/1840/C)                         |       1000 | `L`  |
|   5 | [CF 1690D — Black and White Stripe](https://codeforces.com/problemset/problem/1690/D)             |       1000 | `R`  |
|   6 | [CF 1744C — Traffic Light](https://codeforces.com/problemset/problem/1744/C)                      |       1000 | `R`  |
|   7 | [CF 1669F — Eating Candies](https://codeforces.com/problemset/problem/1669/F)                     |       1100 | `R`  |
|   8 | [CF 489B — BerSU Ball](https://codeforces.com/problemset/problem/489/B)                           |       1200 | `H`  |
|   9 | [CF 600B — Queries about less or equal elements](https://codeforces.com/problemset/problem/600/B) |       1300 | `F`  |
|  10 | [CF 580B — Kefa and Company](https://codeforces.com/problemset/problem/580/B)                     |       1500 | `X`  |

## 8. Бинарный/тернарный поиск и поиск по ответу

Приоритет **A**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 8](ROADMAP.md#тема-8).

База LeetCode, не входит в лимит: [LC 704 — Binary Search](https://leetcode.com/problems/binary-search/); [LC 875 — Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/).

|   № | Задача                                                                                 | Рейтинг CF | Роль |
| --: | -------------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [ACMP 267 — Ксерокопии](https://acmp.ru/index.asp?main=task&id_task=267)               |          — | `D`  |
|   2 | [ACMP 523 — Роман в томах](https://acmp.ru/index.asp?main=task&id_task=523)            |          — | `L`  |
|   3 | [CF 1138A — Sushi for Two](https://codeforces.com/problemset/problem/1138/A)           |        900 | `L`  |
|   4 | [CF 706B — Interesting drink](https://codeforces.com/problemset/problem/706/B)         |       1100 | `L`  |
|   5 | [CF 1873E — Building an Aquarium](https://codeforces.com/problemset/problem/1873/E)    |       1100 | `R`  |
|   6 | [CF 1490C — Sum of Cubes](https://codeforces.com/problemset/problem/1490/C)            |       1100 | `R`  |
|   7 | [CF 1352C — K-th Not Divisible by n](https://codeforces.com/problemset/problem/1352/C) |       1200 | `R`  |
|   8 | [CF 474B — Worms](https://codeforces.com/problemset/problem/474/B)                     |       1200 | `H`  |
|   9 | [CF 1742E — Scuza](https://codeforces.com/problemset/problem/1742/E)                   |       1200 | `F`  |
|  10 | [CF 230B — T-primes](https://codeforces.com/problemset/problem/230/B)                  |       1300 | `X`  |

## 9. Жадные алгоритмы, инварианты и обменный аргумент

Приоритет **A**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 9](ROADMAP.md#тема-9).

База LeetCode, не входит в лимит: [LC 55 — Jump Game](https://leetcode.com/problems/jump-game/); [LC 435 — Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/).

|   № | Задача                                                                                  | Рейтинг CF | Роль |
| --: | --------------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [ACMP 39 — Волосатый бизнес](https://acmp.ru/index.asp?main=task&id_task=39)            |          — | `D`  |
|   2 | [ACMP 228 — Валютные махинации](https://acmp.ru/index.asp?main=task&id_task=228)        |          — | `L`  |
|   3 | [CF 337A — Puzzles](https://codeforces.com/problemset/problem/337/A)                    |        900 | `L`  |
|   4 | [CF 34B — Sale](https://codeforces.com/problemset/problem/34/B)                         |        900 | `L`  |
|   5 | [CF 58A — Chat room](https://codeforces.com/problemset/problem/58/A)                    |       1000 | `R`  |
|   6 | [CF 158B — Taxi](https://codeforces.com/problemset/problem/158/B)                       |       1100 | `R`  |
|   7 | [CF 514A — Chewbaсca and Number](https://codeforces.com/problemset/problem/514/A)       |       1200 | `R`  |
|   8 | [CF 1294C — Product of Three Numbers](https://codeforces.com/problemset/problem/1294/C) |       1300 | `H`  |
|   9 | [CF 550A — Two Substrings](https://codeforces.com/problemset/problem/550/A)             |       1500 | `F`  |
|  10 | [CF 1365D — Solve The Maze](https://codeforces.com/problemset/problem/1365/D)           |       1700 | `X`  |

## 10. Биты, маски, подмаски и булева алгебра

Приоритет **A**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 10](ROADMAP.md#тема-10).

База LeetCode, не входит в лимит: [LC 78 — Subsets](https://leetcode.com/problems/subsets/); [LC 1310 — XOR Queries of a Subarray](https://leetcode.com/problems/xor-queries-of-a-subarray/).

|   № | Задача                                                                                     | Рейтинг CF | Роль |
| --: | ------------------------------------------------------------------------------------------ | ---------: | :--: |
|   1 | [ACMP 542 — Бит-реверс](https://acmp.ru/index.asp?main=task&id_task=542)                   |          — | `D`  |
|   2 | [ACMP 563 — Задача про XOR](https://acmp.ru/index.asp?main=task&id_task=563)               |          — | `L`  |
|   3 | [CF 1559A — Mocha and Math](https://codeforces.com/problemset/problem/1559/A)              |        900 | `L`  |
|   4 | [CF 579A — Raising Bacteria](https://codeforces.com/problemset/problem/579/A)              |       1000 | `L`  |
|   5 | [CF 467B — Fedor and New Game](https://codeforces.com/problemset/problem/467/B)            |       1100 | `R`  |
|   6 | [CF 1420B — Rock and Lever](https://codeforces.com/problemset/problem/1420/B)              |       1200 | `R`  |
|   7 | [CF 1097B — Petr and a Combination Lock](https://codeforces.com/problemset/problem/1097/B) |       1200 | `R`  |
|   8 | [CF 476B — Dreamoon and WiFi](https://codeforces.com/problemset/problem/476/B)             |       1300 | `H`  |
|   9 | [CF 1516B — AGAGA XOOORRR](https://codeforces.com/problemset/problem/1516/B)               |       1500 | `F`  |
|  10 | [CF 276D — Little Girl and Maximum XOR](https://codeforces.com/problemset/problem/276/D)   |       1700 | `X`  |

## 11. Теория чисел: gcd, простые, факторизация, решето

Приоритет **A**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 11](ROADMAP.md#тема-11).

База LeetCode, не входит в лимит: [LC 204 — Count Primes](https://leetcode.com/problems/count-primes/); [LC 1979 — Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/).

|   № | Задача                                                                                                  | Рейтинг CF | Роль |
| --: | ------------------------------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [ACMP 14 — НОК](https://acmp.ru/index.asp?main=task&id_task=14)                                         |          — | `D`  |
|   2 | [ACMP 170 — Разложение числа](https://acmp.ru/index.asp?main=task&id_task=170)                          |          — | `L`  |
|   3 | [CF 1475A — Odd Divisor](https://codeforces.com/problemset/problem/1475/A)                              |        900 | `L`  |
|   4 | [CF 313A — Ilya and Bank Account](https://codeforces.com/problemset/problem/313/A)                      |        900 | `L`  |
|   5 | [CF 1855B — Longest Divisors Interval](https://codeforces.com/problemset/problem/1855/B)                |        900 | `R`  |
|   6 | [CF 742A — Arpa’s hard exam and Mehrdad’s naive cheat](https://codeforces.com/problemset/problem/742/A) |       1000 | `R`  |
|   7 | [CF 1742D — Coprime](https://codeforces.com/problemset/problem/1742/D)                                  |       1100 | `R`  |
|   8 | [CF 1542B — Plus and Multiply](https://codeforces.com/problemset/problem/1542/B)                        |       1500 | `H`  |
|   9 | [CF 1538D — Another Problem About Dividing Numbers](https://codeforces.com/problemset/problem/1538/D)   |       1700 | `F`  |
|  10 | [CF 1627D — Not Adding](https://codeforces.com/problemset/problem/1627/D)                               |       1900 | `X`  |

## 12. Модульная арифметика и комбинаторика

Приоритет **A**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 12](ROADMAP.md#тема-12).

База LeetCode, не входит в лимит: [LC 62 — Unique Paths](https://leetcode.com/problems/unique-paths/); [LC 1641 — Count Sorted Vowel Strings](https://leetcode.com/problems/count-sorted-vowel-strings/).

|   № | Задача                                                                                           | Рейтинг CF | Роль |
| --: | ------------------------------------------------------------------------------------------------ | ---------: | :--: |
|   1 | [ACMP 158 — Великий комбинатор](https://acmp.ru/index.asp?main=task&id_task=158)                 |          — | `D`  |
|   2 | [ACMP 629 — Сочетания](https://acmp.ru/index.asp?main=task&id_task=629)                          |          — | `L`  |
|   3 | [CF 1917B — Erase First or Second Letter](https://codeforces.com/problemset/problem/1917/B)      |       1100 | `L`  |
|   4 | [CF 1514B — AND 0, Sum Big](https://codeforces.com/problemset/problem/1514/B)                    |       1200 | `L`  |
|   5 | [CF 459B — Pashmak and Flowers](https://codeforces.com/problemset/problem/459/B)                 |       1300 | `R`  |
|   6 | [CF 478B — Random Teams](https://codeforces.com/problemset/problem/478/B)                        |       1300 | `R`  |
|   7 | [CF 1931D — Divisible Pairs](https://codeforces.com/problemset/problem/1931/D)                   |       1300 | `R`  |
|   8 | [CF 414B — Mashmokh and ACM](https://codeforces.com/problemset/problem/414/B)                    |       1400 | `H`  |
|   9 | [CF 1305C — Kuroni and Impossible Calculation](https://codeforces.com/problemset/problem/1305/C) |       1600 | `F`  |
|  10 | [CF 300C — Beautiful Numbers](https://codeforces.com/problemset/problem/300/C)                   |       1800 | `X`  |

## 13. Строки: префикс-функция, Z-функция и хеширование

Приоритет **A**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 13](ROADMAP.md#тема-13).

База LeetCode, не входит в лимит: [LC 28 — Find the Index of the First Occurrence](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/); [LC 214 — Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/).

|   № | Задача                                                                           | Рейтинг CF | Роль |
| --: | -------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [ACMP 202 — Поиск подстроки](https://acmp.ru/index.asp?main=task&id_task=202)    |          — | `D`  |
|   2 | [ACMP 204 — Циклическая строка](https://acmp.ru/index.asp?main=task&id_task=204) |          — | `L`  |
|   3 | [CF 96A — Football](https://codeforces.com/problemset/problem/96/A)              |        900 | `L`  |
|   4 | [CF 208A — Dubstep](https://codeforces.com/problemset/problem/208/A)             |        900 | `L`  |
|   5 | [CF 43A — Football](https://codeforces.com/problemset/problem/43/A)              |       1000 | `R`  |
|   6 | [CF 126B — Password](https://codeforces.com/problemset/problem/126/B)            |       1700 | `R`  |
|   7 | [CF 471D — MUH and Cube Walls](https://codeforces.com/problemset/problem/471/D)  |       1800 | `R`  |
|   8 | [CF 535D — Tavas and Malekas](https://codeforces.com/problemset/problem/535/D)   |       1900 | `H`  |
|   9 | [CF 1200E — Compress Words](https://codeforces.com/problemset/problem/1200/E)    |       2000 | `F`  |
|  10 | [CF 7D — Palindrome Degree](https://codeforces.com/problemset/problem/7/D)       |       2200 | `X`  |

## 14. Обходы графа, компоненты, циклы и двудольность

Приоритет **A**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 14](ROADMAP.md#тема-14).

База LeetCode, не входит в лимит: [LC 200 — Number of Islands](https://leetcode.com/problems/number-of-islands/); [LC 785 — Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/).

|   № | Задача                                                                               | Рейтинг CF | Роль |
| --: | ------------------------------------------------------------------------------------ | ---------: | :--: |
|   1 | [ACMP 15 — Дороги](https://acmp.ru/index.asp?main=task&id_task=15)                   |          — | `D`  |
|   2 | [ACMP 99 — Лабиринт](https://acmp.ru/index.asp?main=task&id_task=99)                 |          — | `L`  |
|   3 | [CF 115A — Party](https://codeforces.com/problemset/problem/115/A)                   |        900 | `L`  |
|   4 | [CF 500A — New Year Transportation](https://codeforces.com/problemset/problem/500/A) |       1000 | `L`  |
|   5 | [CF 1829E — The Lakes](https://codeforces.com/problemset/problem/1829/E)             |       1100 | `R`  |
|   6 | [CF 445A — DZY Loves Chessboard](https://codeforces.com/problemset/problem/445/A)    |       1200 | `R`  |
|   7 | [CF 1433D — Districts Connection](https://codeforces.com/problemset/problem/1433/D)  |       1200 | `R`  |
|   8 | [CF 893C — Rumor](https://codeforces.com/problemset/problem/893/C)                   |       1300 | `H`  |
|   9 | [CF 1702E — Split Into Two Sets](https://codeforces.com/problemset/problem/1702/E)   |       1600 | `F`  |
|  10 | [CF 377A — Maze](https://codeforces.com/problemset/problem/377/A)                    |       1600 | `X`  |

## 15. Кратчайшие пути: BFS, 0–1 BFS, Дейкстра, Флойд, Беллман—Форд

Приоритет **A**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 15](ROADMAP.md#тема-15).

База LeetCode, не входит в лимит: [LC 743 — Network Delay Time](https://leetcode.com/problems/network-delay-time/); [LC 787 — Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/).

|   № | Задача                                                                             | Рейтинг CF | Роль |
| --: | ---------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [ACMP 132 — Алгоритм Дейкстры](https://acmp.ru/index.asp?main=task&id_task=132)    |          — | `D`  |
|   2 | [ACMP 135 — Алгоритм Флойда](https://acmp.ru/index.asp?main=task&id_task=135)      |          — | `L`  |
|   3 | [CF 3A — Shortest path of the king](https://codeforces.com/problemset/problem/3/A) |       1000 | `L`  |
|   4 | [CF 1661B — Getting Zero](https://codeforces.com/problemset/problem/1661/B)        |       1300 | `L`  |
|   5 | [CF 520B — Two Buttons](https://codeforces.com/problemset/problem/520/B)           |       1400 | `R`  |
|   6 | [CF 1418C — Mortal Kombat Tower](https://codeforces.com/problemset/problem/1418/C) |       1500 | `R`  |
|   7 | [CF 295B — Greg and Graph](https://codeforces.com/problemset/problem/295/B)        |       1700 | `R`  |
|   8 | [CF 242C — King's Path](https://codeforces.com/problemset/problem/242/C)           |       1800 | `H`  |
|   9 | [CF 20C — Dijkstra?](https://codeforces.com/problemset/problem/20/C)               |       1900 | `F`  |
|  10 | [CF 449B — Jzzhu and Cities](https://codeforces.com/problemset/problem/449/B)      |       2000 | `X`  |

## 16. Деревья: Эйлеров обход, двоичные подъёмы и LCA

Приоритет **A**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 16](ROADMAP.md#тема-16).

База LeetCode, не входит в лимит: [LC 236 — Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/); [LC 863 — All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/).

|   № | Задача                                                                                              | Рейтинг CF | Роль |
| --: | --------------------------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [ACMP 141 — Дерево](https://acmp.ru/index.asp?main=task&id_task=141)                                |          — | `D`  |
|   2 | [CF 1511C — Yet Another Card Deck](https://codeforces.com/problemset/problem/1511/C)                |       1100 | `L`  |
|   3 | [CF 1843D — Apple Tree](https://codeforces.com/problemset/problem/1843/D)                           |       1200 | `L`  |
|   4 | [CF 862B — Mahmoud and Ehab and the bipartiteness](https://codeforces.com/problemset/problem/862/B) |       1300 | `L`  |
|   5 | [CF 1676G — White-Black Balanced Subtrees](https://codeforces.com/problemset/problem/1676/G)        |       1300 | `R`  |
|   6 | [CF 580C — Kefa and Park](https://codeforces.com/problemset/problem/580/C)                          |       1500 | `R`  |
|   7 | [CF 1037D — Valid BFS?](https://codeforces.com/problemset/problem/1037/D)                           |       1700 | `R`  |
|   8 | [CF 1328E — Tree Queries](https://codeforces.com/problemset/problem/1328/E)                         |       1900 | `H`  |
|   9 | [CF 1304E — 1-Trees and Queries](https://codeforces.com/problemset/problem/1304/E)                  |       2000 | `F`  |
|  10 | [CF 519E — A and B and Lecture Rooms](https://codeforces.com/problemset/problem/519/E)              |       2100 | `X`  |

## 17. Базовое DP: пути, рюкзак, LIS и восстановление ответа

Приоритет **A**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 17](ROADMAP.md#тема-17).

База LeetCode, не входит в лимит: [LC 322 — Coin Change](https://leetcode.com/problems/coin-change/); [LC 300 — Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/).

|   № | Задача                                                                             | Рейтинг CF | Роль |
| --: | ---------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [ACMP 11 — Зайчик](https://acmp.ru/index.asp?main=task&id_task=11)                 |          — | `D`  |
|   2 | [ACMP 121 — Гвоздики](https://acmp.ru/index.asp?main=task&id_task=121)             |          — | `L`  |
|   3 | [CF 580A — Kefa and First Steps](https://codeforces.com/problemset/problem/580/A)  |        900 | `L`  |
|   4 | [CF 1475B — New Year's Number](https://codeforces.com/problemset/problem/1475/B)   |        900 | `L`  |
|   5 | [CF 189A — Cut Ribbon](https://codeforces.com/problemset/problem/189/A)            |       1300 | `R`  |
|   6 | [CF 1195C — Basketball Exercise](https://codeforces.com/problemset/problem/1195/C) |       1400 | `R`  |
|   7 | [CF 698A — Vacations](https://codeforces.com/problemset/problem/698/A)             |       1400 | `R`  |
|   8 | [CF 455A — Boredom](https://codeforces.com/problemset/problem/455/A)               |       1500 | `H`  |
|   9 | [CF 706C — Hard problem](https://codeforces.com/problemset/problem/706/C)          |       1600 | `F`  |
|  10 | [CF 474D — Flowers](https://codeforces.com/problemset/problem/474/D)               |       1700 | `X`  |

## 18. Fenwick, segment tree, lazy propagation и sparse table

Приоритет **A**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 18](ROADMAP.md#тема-18).

База LeetCode, не входит в лимит: [LC 307 — Range Sum Query — Mutable](https://leetcode.com/problems/range-sum-query-mutable/); [LC 715 — Range Module](https://leetcode.com/problems/range-module/).

|   № | Задача                                                                                     | Рейтинг CF | Роль |
| --: | ------------------------------------------------------------------------------------------ | ---------: | :--: |
|   1 | [ACMP 112 — Армия](https://acmp.ru/index.asp?main=task&id_task=112)                        |          — | `D`  |
|   2 | [ACMP 418 — Редактор](https://acmp.ru/index.asp?main=task&id_task=418)                     |          — | `L`  |
|   3 | [CF 339D — Xenia and Bit Operations](https://codeforces.com/problemset/problem/339/D)      |       1700 | `L`  |
|   4 | [CF 459D — Pashmak and Parmida's problem](https://codeforces.com/problemset/problem/459/D) |       1800 | `L`  |
|   5 | [CF 61E — Enemy is weak](https://codeforces.com/problemset/problem/61/E)                   |       1900 | `R`  |
|   6 | [CF 380C — Sereja and Brackets](https://codeforces.com/problemset/problem/380/C)           |       2000 | `R`  |
|   7 | [CF 242E — XOR on Segment](https://codeforces.com/problemset/problem/242/E)                |       2000 | `R`  |
|   8 | [CF 474F — Ant colony](https://codeforces.com/problemset/problem/474/F)                    |       2100 | `H`  |
|   9 | [CF 52C — Circular RMQ](https://codeforces.com/problemset/problem/52/C)                    |       2200 | `F`  |
|  10 | [CF 438D — The Child and Sequence](https://codeforces.com/problemset/problem/438/D)        |       2300 | `X`  |

## 19. Вычислительная геометрия

Приоритет **B**. Задач: **7**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 19](ROADMAP.md#тема-19).

База LeetCode, не входит в лимит: [LC 973 — K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/); [LC 149 — Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/).

|   № | Задача                                                                                    | Рейтинг CF | Роль |
| --: | ----------------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [ACMP 348 — Пересечение отрезков](https://acmp.ru/index.asp?main=task&id_task=348)        |          — | `D`  |
|   2 | [CF 766B — Mahmoud and a Triangle](https://codeforces.com/problemset/problem/766/B)       |       1000 | `L`  |
|   3 | [CF 507B — Amr and Pins](https://codeforces.com/problemset/problem/507/B)                 |       1400 | `L`  |
|   4 | [CF 514B — Han Solo and Lazer Gun](https://codeforces.com/problemset/problem/514/B)       |       1400 | `R`  |
|   5 | [CF 1486B — Eastern Exhibition](https://codeforces.com/problemset/problem/1486/B)         |       1500 | `H`  |
|   6 | [CF 1730B — Meeting on the Line](https://codeforces.com/problemset/problem/1730/B)        |       1600 | `F`  |
|   7 | [CF 1552C — Maximize the Intersections](https://codeforces.com/problemset/problem/1552/C) |       1800 | `X`  |

## 20. DAG, топосортировка, SCC, мосты и точки сочленения

Приоритет **B**. Задач: **7**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 20](ROADMAP.md#тема-20).

База LeetCode, не входит в лимит: [LC 1192 — Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/); [LC 802 — Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/).

|   № | Задача                                                                             | Рейтинг CF | Роль |
| --: | ---------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [ACMP 124 — Светофорчики](https://acmp.ru/index.asp?main=task&id_task=124)         |          — | `D`  |
|   2 | [CF 977E — Cyclic Components](https://codeforces.com/problemset/problem/977/E)     |       1500 | `L`  |
|   3 | [CF 687A — NP-Hard Problem](https://codeforces.com/problemset/problem/687/A)       |       1500 | `L`  |
|   4 | [CF 510C — Fox And Names](https://codeforces.com/problemset/problem/510/C)         |       1600 | `R`  |
|   5 | [CF 427C — Checkposts](https://codeforces.com/problemset/problem/427/C)            |       1700 | `H`  |
|   6 | [CF 118E — Bertown roads](https://codeforces.com/problemset/problem/118/E)         |       2000 | `F`  |
|   7 | [CF 1000E — We Need More Bosses](https://codeforces.com/problemset/problem/1000/E) |       2100 | `X`  |

## 21. DSU, MST и офлайн-связность

Приоритет **B**. Задач: **7**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 21](ROADMAP.md#тема-21).

База LeetCode, не входит в лимит: [LC 1584 — Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/); [LC 721 — Accounts Merge](https://leetcode.com/problems/accounts-merge/).

|   № | Задача                                                                                           | Рейтинг CF | Роль |
| --: | ------------------------------------------------------------------------------------------------ | ---------: | :--: |
|   1 | [ACMP 142 — Минимальный каркас](https://acmp.ru/index.asp?main=task&id_task=142)                 |          — | `D`  |
|   2 | [CF 1249B2 — Books Exchange (hard version)](https://codeforces.com/problemset/problem/1249/B2)   |       1300 | `L`  |
|   3 | [CF 277A — Learning Languages](https://codeforces.com/problemset/problem/277/A)                  |       1400 | `L`  |
|   4 | [CF 1167C — News Distribution](https://codeforces.com/problemset/problem/1167/C)                 |       1400 | `R`  |
|   5 | [CF 25D — Roads not only in Berland](https://codeforces.com/problemset/problem/25/D)             |       1900 | `H`  |
|   6 | [CF 609E — Minimum spanning tree for each edge](https://codeforces.com/problemset/problem/609/E) |       2100 | `F`  |
|   7 | [CF 160D — Edges in MST](https://codeforces.com/problemset/problem/160/D)                        |       2300 | `X`  |

## 22. DP по отрезкам, решёткам, графам и деревьям

Приоритет **B**. Задач: **7**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 22](ROADMAP.md#тема-22).

База LeetCode, не входит в лимит: [LC 312 — Burst Balloons](https://leetcode.com/problems/burst-balloons/); [LC 337 — House Robber III](https://leetcode.com/problems/house-robber-iii/).

|   № | Задача                                                                                | Рейтинг CF | Роль |
| --: | ------------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [ACMP 123 — Восстановление скобок](https://acmp.ru/index.asp?main=task&id_task=123)   |          — | `D`  |
|   2 | [CF 1528A — Parsa's Humongous Tree](https://codeforces.com/problemset/problem/1528/A) |       1600 | `L`  |
|   3 | [CF 1249E — By Elevator or Stairs?](https://codeforces.com/problemset/problem/1249/E) |       1700 | `L`  |
|   4 | [CF 161D — Distance in Tree](https://codeforces.com/problemset/problem/161/D)         |       1800 | `R`  |
|   5 | [CF 607B — Zuma](https://codeforces.com/problemset/problem/607/B)                     |       1900 | `H`  |
|   6 | [CF 1114D — Flood Fill](https://codeforces.com/problemset/problem/1114/D)             |       1900 | `F`  |
|   7 | [CF 1363E — Tree Shuffling](https://codeforces.com/problemset/problem/1363/E)         |       2000 | `X`  |

## 23. DP по подмножествам, цифрам и профилю

Приоритет **B**. Задач: **7**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 23](ROADMAP.md#тема-23).

База LeetCode, не входит в лимит: [LC 464 — Can I Win](https://leetcode.com/problems/can-i-win/); [LC 902 — Numbers At Most N Given Digit Set](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/).

|   № | Задача                                                                          | Рейтинг CF | Роль |
| --: | ------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [ACMP 29 — Компьютерная игра](https://acmp.ru/index.asp?main=task&id_task=29)   |          — | `D`  |
|   2 | [CF 580D — Kefa and Dishes](https://codeforces.com/problemset/problem/580/D)    |       1800 | `L`  |
|   3 | [CF 577B — Modulo Sum](https://codeforces.com/problemset/problem/577/B)         |       1900 | `L`  |
|   4 | [CF 1288D — Minimax Problem](https://codeforces.com/problemset/problem/1288/D)  |       2000 | `R`  |
|   5 | [CF 165E — Compatible Numbers](https://codeforces.com/problemset/problem/165/E) |       2200 | `H`  |
|   6 | [CF 628D — Magic Numbers](https://codeforces.com/problemset/problem/628/D)      |       2200 | `F`  |
|   7 | [CF 55D — Beautiful numbers](https://codeforces.com/problemset/problem/55/D)    |       2500 | `X`  |

## 24. Декартово дерево, treap и порядковые структуры

Приоритет **B**. Задач: **7**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 24](ROADMAP.md#тема-24).

База LeetCode, не входит в лимит: [LC 315 — Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/); [LC 327 — Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/).

|   № | Задача                                                                                            | Рейтинг CF | Роль |
| --: | ------------------------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [ACMP 505 — Забор](https://acmp.ru/index.asp?main=task&id_task=505)                               |          — | `D`  |
|   2 | [CF 706D — Vasiliy's Multiset](https://codeforces.com/problemset/problem/706/D)                   |       1800 | `L`  |
|   3 | [CF 1354D — Multiset](https://codeforces.com/problemset/problem/1354/D)                           |       1900 | `L`  |
|   4 | [CF 915E — Physical Education Lessons](https://codeforces.com/problemset/problem/915/E)           |       2300 | `R`  |
|   5 | [CF 558E — A Simple Task](https://codeforces.com/problemset/problem/558/E)                        |       2300 | `H`  |
|   6 | [CF 1748E — Yet Another Array Counting Problem](https://codeforces.com/problemset/problem/1748/E) |       2300 | `F`  |
|   7 | [CF 702F — T-Shirts](https://codeforces.com/problemset/problem/702/F)                             |       2800 | `X`  |

## 25. Потоки и паросочетания

Приоритет **B**. Задач: **7**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 25](ROADMAP.md#тема-25).

База LeetCode, не входит в лимит: [LC 1820 — Maximum Number of Accepted Invitations](https://leetcode.com/problems/maximum-number-of-accepted-invitations/); [LC 1066 — Campus Bikes II](https://leetcode.com/problems/campus-bikes-ii/).

|   № | Задача                                                                               | Рейтинг CF | Роль |
| --: | ------------------------------------------------------------------------------------ | ---------: | :--: |
|   1 | [ACMP 151 — Банкет](https://acmp.ru/index.asp?main=task&id_task=151)                 |          — | `D`  |
|   2 | [CF 1530D — Secret Santa](https://codeforces.com/problemset/problem/1530/D)          |       1600 | `L`  |
|   3 | [CF 1525D — Armchairs](https://codeforces.com/problemset/problem/1525/D)             |       1800 | `L`  |
|   4 | [CF 1437C — Chef Monocarp](https://codeforces.com/problemset/problem/1437/C)         |       1800 | `R`  |
|   5 | [CF 1426E — Rock, Paper, Scissors](https://codeforces.com/problemset/problem/1426/E) |       1800 | `H`  |
|   6 | [CF 468B — Two Sets](https://codeforces.com/problemset/problem/468/B)                |       2000 | `F`  |
|   7 | [CF 546E — Soldier and Traveling](https://codeforces.com/problemset/problem/546/E)   |       2100 | `X`  |

## 26. Ахо—Корасик, Манакер, suffix array/automaton

Приоритет **B**. Задач: **7**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 26](ROADMAP.md#тема-26).

База LeetCode, не входит в лимит: [LC 1044 — Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/); [LC 336 — Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/).

|   № | Задача                                                                                                   | Рейтинг CF | Роль |
| --: | -------------------------------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [ACMP 70 — Степень строки](https://acmp.ru/index.asp?main=task&id_task=70)                               |          — | `D`  |
|   2 | [CF 559B — Equivalent Strings](https://codeforces.com/problemset/problem/559/B)                          |       1700 | `L`  |
|   3 | [CF 271D — Good Substrings](https://codeforces.com/problemset/problem/271/D)                             |       1800 | `L`  |
|   4 | [CF 1326D2 — Prefix-Suffix Palindrome (Hard version)](https://codeforces.com/problemset/problem/1326/D2) |       1800 | `R`  |
|   5 | [CF 432D — Prefixes and Suffixes](https://codeforces.com/problemset/problem/432/D)                       |       2000 | `H`  |
|   6 | [CF 710F — String Set Queries](https://codeforces.com/problemset/problem/710/F)                          |       2400 | `F`  |
|   7 | [CF 873F — Forbidden Indices](https://codeforces.com/problemset/problem/873/F)                           |       2400 | `X`  |

## 27. HLD, центроидная декомпозиция, small-to-large и rerooting

Приоритет **B**. Задач: **7**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 27](ROADMAP.md#тема-27).

База LeetCode, не входит в лимит: [LC 834 — Sum of Distances in Tree](https://leetcode.com/problems/sum-of-distances-in-tree/); [LC 1483 — Kth Ancestor of a Tree Node](https://leetcode.com/problems/kth-ancestor-of-a-tree-node/).

|   № | Задача                                                                          | Рейтинг CF | Роль |
| --: | ------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [ACMP 116 — Фермер - 2](https://acmp.ru/index.asp?main=task&id_task=116)        |          — | `D`  |
|   2 | [CF 191C — Fools and Roads](https://codeforces.com/problemset/problem/191/C)    |       1900 | `L`  |
|   3 | [CF 383C — Propagating tree](https://codeforces.com/problemset/problem/383/C)   |       2000 | `L`  |
|   4 | [CF 321C — Ciel the Commander](https://codeforces.com/problemset/problem/321/C) |       2100 | `R`  |
|   5 | [CF 600E — Lomsat gelral](https://codeforces.com/problemset/problem/600/E)      |       2300 | `H`  |
|   6 | [CF 342E — Xenia and Tree](https://codeforces.com/problemset/problem/342/E)     |       2400 | `F`  |
|   7 | [CF 375D — Tree and Queries](https://codeforces.com/problemset/problem/375/D)   |       2400 | `X`  |

## 28. Теория игр: выигрыш/проигрыш, Nim и Sprague—Grundy

Приоритет **B**. Задач: **7**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 28](ROADMAP.md#тема-28).

База LeetCode, не входит в лимит: [LC 292 — Nim Game](https://leetcode.com/problems/nim-game/); [LC 486 — Predict the Winner](https://leetcode.com/problems/predict-the-winner/).

|   № | Задача                                                                                          | Рейтинг CF | Роль |
| --: | ----------------------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [ACMP 4 — Игра](https://acmp.ru/index.asp?main=task&id_task=4)                                  |          — | `D`  |
|   2 | [CF 1527B1 — Palindrome Game (easy version)](https://codeforces.com/problemset/problem/1527/B1) |       1200 | `L`  |
|   3 | [CF 1747C — Swap Game](https://codeforces.com/problemset/problem/1747/C)                        |       1200 | `L`  |
|   4 | [CF 1472D — Even-Odd Game](https://codeforces.com/problemset/problem/1472/D)                    |       1200 | `R`  |
|   5 | [CF 276B — Little Girl and Game](https://codeforces.com/problemset/problem/276/B)               |       1300 | `H`  |
|   6 | [CF 1370C — Number Game](https://codeforces.com/problemset/problem/1370/C)                      |       1400 | `F`  |
|   7 | [CF 1363C — Game On Leaves](https://codeforces.com/problemset/problem/1363/C)                   |       1600 | `X`  |

## 29. Meet-in-the-middle и разбиение пространства поиска

Приоритет **B**. Задач: **7**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 29](ROADMAP.md#тема-29).

База LeetCode, не входит в лимит: [LC 1755 — Closest Subsequence Sum](https://leetcode.com/problems/closest-subsequence-sum/).

|   № | Задача                                                                                       | Рейтинг CF | Роль |
| --: | -------------------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [CF 769D — k-Interesting Pairs Of Integers](https://codeforces.com/problemset/problem/769/D) |       1700 | `D`  |
|   2 | [CF 888E — Maximum Subsequence](https://codeforces.com/problemset/problem/888/E)             |       1800 | `L`  |
|   3 | [CF 552C — Vanya and Scales](https://codeforces.com/problemset/problem/552/C)                |       1900 | `L`  |
|   4 | [CF 1006F — Xor-Paths](https://codeforces.com/problemset/problem/1006/F)                     |       2100 | `R`  |
|   5 | [CF 525E — Anya and Cubes](https://codeforces.com/problemset/problem/525/E)                  |       2100 | `H`  |
|   6 | [CF 1105E — Helping Hiasat ](https://codeforces.com/problemset/problem/1105/E)               |       2200 | `F`  |
|   7 | [CF 1257F — Make Them Similar](https://codeforces.com/problemset/problem/1257/F)             |       2400 | `X`  |

## 30. Корневая декомпозиция, Mo и офлайн-запросы

Приоритет **C**. Задач: **5**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 30](ROADMAP.md#тема-30).

База LeetCode, не входит в лимит: [LC 493 — Reverse Pairs](https://leetcode.com/problems/reverse-pairs/).

|   № | Задача                                                                                 | Рейтинг CF | Роль |
| --: | -------------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [CF 220B — Little Elephant and Array](https://codeforces.com/problemset/problem/220/B) |       1800 | `L`  |
|   2 | [CF 86D — Powerful array](https://codeforces.com/problemset/problem/86/D)              |       2200 | `R`  |
|   3 | [CF 617E — XOR and Favorite Number](https://codeforces.com/problemset/problem/617/E)   |       2200 | `H`  |
|   4 | [CF 13E — Holes](https://codeforces.com/problemset/problem/13/E)                       |       2700 | `F`  |
|   5 | [CF 455D — Serega and Fun](https://codeforces.com/problemset/problem/455/D)            |       2700 | `X`  |

## 31. Rollback, персистентность и динамическая связность

Приоритет **C**. Задач: **5**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 31](ROADMAP.md#тема-31).

База LeetCode, не входит в лимит: [LC 1146 — Snapshot Array](https://leetcode.com/problems/snapshot-array/).

|   № | Задача                                                                            | Рейтинг CF | Роль |
| --: | --------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [CF 292D — Connected Components](https://codeforces.com/problemset/problem/292/D) |       1900 | `L`  |
|   2 | [CF 707D — Persistent Bookcase](https://codeforces.com/problemset/problem/707/D)  |       2200 | `R`  |
|   3 | [CF 813E — Army Creation](https://codeforces.com/problemset/problem/813/E)        |       2200 | `H`  |
|   4 | [CF 891C — Envy](https://codeforces.com/problemset/problem/891/C)                 |       2300 | `F`  |
|   5 | [CF 484E — Sign on Fence](https://codeforces.com/problemset/problem/484/E)        |       2500 | `X`  |

## 32. Оптимизации DP: CHT/Li Chao, divide-and-conquer, Knuth

Приоритет **C**. Задач: **5**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 32](ROADMAP.md#тема-32).

База LeetCode, не входит в лимит: [LC 410 — Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/).

|   № | Задача                                                                                                | Рейтинг CF | Роль |
| --: | ----------------------------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [CF 319C — Kalila and Dimna in the Logging Industry](https://codeforces.com/problemset/problem/319/C) |       2100 | `L`  |
|   2 | [CF 1083E — The Fair Nut and Rectangles](https://codeforces.com/problemset/problem/1083/E)            |       2400 | `R`  |
|   3 | [CF 868F — Yet Another Minimization Problem](https://codeforces.com/problemset/problem/868/F)         |       2500 | `H`  |
|   4 | [CF 321E — Ciel and Gondolas](https://codeforces.com/problemset/problem/321/E)                        |       2600 | `F`  |
|   5 | [CF 932F — Escape Through Leaf](https://codeforces.com/problemset/problem/932/F)                      |       2700 | `X`  |

## 33. Матрицы, линейная алгебра, FFT/NTT

Приоритет **C**. Задач: **5**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 33](ROADMAP.md#тема-33).

База LeetCode, не входит в лимит: [LC 509 — Fibonacci Number](https://leetcode.com/problems/fibonacci-number/); [LC 43 — Multiply Strings](https://leetcode.com/problems/multiply-strings/).

|   № | Задача                                                                        | Рейтинг CF | Роль |
| --: | ----------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [CF 1557C — Moamen and XOR](https://codeforces.com/problemset/problem/1557/C) |       1700 | `L`  |
|   2 | [CF 222E — Decoding Genome](https://codeforces.com/problemset/problem/222/E)  |       1900 | `R`  |
|   3 | [CF 1117D — Magic Gems](https://codeforces.com/problemset/problem/1117/D)     |       2100 | `H`  |
|   4 | [CF 718C — Sasha and Array](https://codeforces.com/problemset/problem/718/C)  |       2300 | `F`  |
|   5 | [CF 528D — Fuzzy Search](https://codeforces.com/problemset/problem/528/D)     |       2500 | `X`  |

## 34. Вероятность, рандомизация, interactive и output-only

Приоритет **C**. Задач: **5**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 34](ROADMAP.md#тема-34).

База LeetCode, не входит в лимит: [LC 528 — Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/).

|   № | Задача                                                                                        | Рейтинг CF | Роль |
| --: | --------------------------------------------------------------------------------------------- | ---------: | :--: |
|   1 | [CF 839C — Journey](https://codeforces.com/problemset/problem/839/C)                          |       1500 | `L`  |
|   2 | [CF 453A — Little Pony and Expected Maximum](https://codeforces.com/problemset/problem/453/A) |       1600 | `R`  |
|   3 | [CF 1407C — Chocolate Bunny](https://codeforces.com/problemset/problem/1407/C)                |       1600 | `H`  |
|   4 | [CF 1479A — Searching Local Minimum](https://codeforces.com/problemset/problem/1479/A)        |       1700 | `F`  |
|   5 | [CF 148D — Bag of mice](https://codeforces.com/problemset/problem/148/D)                      |       1800 | `X`  |
