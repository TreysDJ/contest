# Банк задач

Этот каталог построен под календарь «лето → отборы в октябре–ноябре → финалы в марте–апреле». Он не требует решить все задачи подряд.

## Объём и маршрут

- этап A0: **49** задач — инженерная и алгоритмическая база;
- этап A1: **142** задач — основные переносимые олимпиадные паттерны;
- этап B: **80** задач — регулярный финальный слой;
- этап C: **25** задач — выборочная продвинутая практика;
- полный каталог: **296** задач Codeforces/ACMP;
- основной маршрут без `H` и `X`: **227** задач;
- LeetCode-база: **63** задач, в основной лимит не входит.
- практические checkpoints: **7** блоков; помеченные как обязательные входят в освоение A0/A1, но не являются задачами онлайн-судьи.

Роли: `D` — диагностика; `L` — изучение приёма; `R` — закрепление; `H` — трудная задача; `F` — контрольная без подсказок; `X` — сочетание тем. Для быстрого маршрута решать `D/L/R/F`; `H/X` переносить на финальный цикл или брать по слабым местам.

Колонка **«Что тренирует»** описывает целевой учебный способ решения, а не утверждает, что других решений не существует. Для `D/F/X` точный паттерн скрыт: раскрывать его следует только после ограниченной самостоятельной попытки.

## Правила работы

1. До начала темы решить `D` за ограниченное время, не раскрывая паттерн. Если идея не найдена, изучить теорию и перейти к `L`.
2. Если задача дала переносимый вывод, записать его одной короткой строкой в [`NOTES.md`](NOTES.md). Для обычного решения без нового вывода заметка не нужна.
3. `F` решать как мини-контест: без раскрытия паттерна, подсказок и старого кода, с полным тестированием и разбором после сдачи.
4. ACMP используется как русскоязычный вход и тренировка реализации; Codeforces — как основная шкала сложности.
5. Рейтинг Codeforces — ориентир, а не строгий порядок. Релевантность приёма и педагогическая роль важнее рейтинга.
6. Если для фундаментального паттерна нет достаточно прямой задачи CF/Gym/ACMP, выполнить обязательный checkpoint; не заменять его случайной задачей с совпавшим тегом.

## 1. Оценка сложности, Java и аккуратная реализация

Этап **A0**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 1](ROADMAP.md#тема-1).

База LeetCode, не входит в лимит: [LC 412 — Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) — Условия и форматирование вывода; [LC 66 — Plus One](https://leetcode.com/problems/plus-one/) — Перенос разряда в массиве цифр.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [ACMP 1 — A+B](https://acmp.ru/index.asp?main=task&id_task=1) | — | `D` | <details><summary>Показать после попытки</summary>Java: запуск решения и базовый ввод/вывод</details> |
| 2 | [CF 71A — Way Too Long Words](https://codeforces.com/problemset/problem/71/A) | 800 | `L` | Пакетный ввод строк и аккуратная обработка длины |
| 3 | [CF 282A — Bit++](https://codeforces.com/problemset/problem/282/A) | 800 | `L` | Разбор коротких команд и изменение счётчика |
| 4 | [CF 1A — Theatre Square](https://codeforces.com/problemset/problem/1/A) | 1000 | `L` | Потолочное деление и обязательный long при произведении |
| 5 | [ACMP 5 — Статистика](https://acmp.ru/index.asp?main=task&id_task=5) | — | `R` | Массивы, фильтрация и точный формат вывода |
| 6 | [CF 158A — Next Round](https://codeforces.com/problemset/problem/158/A) | 800 | `R` | Граница массива при равных значениях |
| 7 | [CF 263A — Beautiful Matrix](https://codeforces.com/problemset/problem/263/A) | 800 | `R` | Двумерная индексация и расстояние по координатам |
| 8 | [CF 492B — Vanya and Lanterns](https://codeforces.com/problemset/problem/492/B) | 1200 | `H` | Сортировка, граничные случаи и вещественная точность |
| 9 | [CF 118A — String Task](https://codeforces.com/problemset/problem/118/A) | 1000 | `F` | <details><summary>Показать после попытки</summary>Линейная фильтрация строки без лишних объектов</details> |
| 10 | [CF 112A — Petya and Strings](https://codeforces.com/problemset/problem/112/A) | 800 | `X` | <details><summary>Показать после попытки</summary>Нормализация регистра и лексикографическое сравнение</details> |

Отдельная практика, не входит в лимит:

**Java-checkpoint, не входит в лимит задач.**

1. Для типичных n оценить допустимую сложность и память до написания кода.
2. С нуля написать быстрый ввод и считать не менее 200000 целых чисел без Scanner.
3. Проверить long до умножения, безопасный comparator и массовый вывод через StringBuilder.
4. Для глубокого графа выбрать итеративный обход либо письменно обосновать безопасную глубину рекурсии.

## 2. Полный перебор, рекурсия и отсечения

Этап **A0**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 2](ROADMAP.md#тема-2).

База LeetCode, не входит в лимит: [LC 46 — Permutations](https://leetcode.com/problems/permutations/) — Backtracking перестановок; [LC 78 — Subsets](https://leetcode.com/problems/subsets/) — Генерация всех подмножеств.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [CF 214A — System of Equations](https://codeforces.com/problemset/problem/214/A) | 800 | `D` | <details><summary>Показать после попытки</summary>Полный перебор двух переменных по малым ограничениям</details> |
| 2 | [CF 271A — Beautiful Year](https://codeforces.com/problemset/problem/271/A) | 800 | `L` | Последовательный перебор до первого допустимого объекта |
| 3 | [CF 122A — Lucky Division](https://codeforces.com/problemset/problem/122/A) | 1000 | `L` | Перебор небольшого заранее ограниченного семейства |
| 4 | [CF 479A — Expression](https://codeforces.com/problemset/problem/479/A) | 1000 | `L` | Перебор фиксированного числа вариантов формулы |
| 5 | [CF 1097B — Petr and a Combination Lock](https://codeforces.com/problemset/problem/1097/B) | 1200 | `R` | Перебор 2^n вариантов выбора знака |
| 6 | [CF 1108C — Nice Garland](https://codeforces.com/problemset/problem/1108/C) | 1300 | `R` | Перебор перестановок малого алфавита |
| 7 | [CF 1950D — Product of Binary Decimals](https://codeforces.com/problemset/problem/1950/D) | 1100 | `R` | Рекурсивный перебор переходов с memoization |
| 8 | [CF 124B — Permutations](https://codeforces.com/problemset/problem/124/B) | 1400 | `H` | Полный перебор n! перестановок |
| 9 | [ACMP 101 — Магараджа](https://acmp.ru/index.asp?main=task&id_task=101) | — | `F` | <details><summary>Показать после попытки</summary>Backtracking с rollback атакованных линий и клеток</details> |
| 10 | [CF 550B — Preparing Olympiad](https://codeforces.com/problemset/problem/550/B) | 1400 | `X` | <details><summary>Показать после попытки</summary>Перебор подмножеств с несколькими ограничениями</details> |

## 3. Сортировка, компараторы и сжатие координат

Этап **A0**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 3](ROADMAP.md#тема-3).

База LeetCode, не входит в лимит: [LC 912 — Sort an Array](https://leetcode.com/problems/sort-an-array/) — Базовая реализация сортировки; [LC 56 — Merge Intervals](https://leetcode.com/problems/merge-intervals/) — Сортировка и слияние интервалов.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [ACMP 41 — Сортировка подсчетом](https://acmp.ru/index.asp?main=task&id_task=41) | — | `D` | <details><summary>Показать после попытки</summary>Counting sort на малом диапазоне значений</details> |
| 2 | [ACMP 119 — Сортировка времени](https://acmp.ru/index.asp?main=task&id_task=119) | — | `L` | Компаратор объектов по составному временному ключу |
| 3 | [CF 141A — Amusing Joke](https://codeforces.com/problemset/problem/141/A) | 800 | `L` | Сортировка или частоты символов для сравнения мультимножеств |
| 4 | [CF 166A — Rank List](https://codeforces.com/problemset/problem/166/A) | 1100 | `L` | Сортировка пар по двум ключам и обработка равенств |
| 5 | [CF 1849B — Monsters](https://codeforces.com/problemset/problem/1849/B) | 1000 | `R` | Компаратор по вычисляемому ключу и исходному индексу |
| 6 | [CF 1399A — Remove Smallest](https://codeforces.com/problemset/problem/1399/A) | 800 | `R` | Сортировка и локальная проверка соседних элементов |
| 7 | [CF 670C — Cinema](https://codeforces.com/problemset/problem/670/C) | 1300 | `R` | Сжатие значений через частоты и выбор по нескольким критериям |
| 8 | [CF 1201C — Maximum Median](https://codeforces.com/problemset/problem/1201/C) | 1400 | `H` | Сортировка и выравнивание суффикса вокруг медианы |
| 9 | [CF 230A — Dragons](https://codeforces.com/problemset/problem/230/A) | 1000 | `F` | <details><summary>Показать после попытки</summary>Сортировка объектов и последовательный инвариант достижимости</details> |
| 10 | [CF 978F — Mentors](https://codeforces.com/problemset/problem/978/F) | 1500 | `X` | <details><summary>Показать после попытки</summary>Сортировка/сжатие с дублями и возвратом к исходным индексам</details> |

## 4. Частоты, HashMap/HashSet и множества

Этап **A0**. Задач: **9**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 4](ROADMAP.md#тема-4).

База LeetCode, не входит в лимит: [LC 1 — Two Sum](https://leetcode.com/problems/two-sum/) — HashMap: поиск дополнения; [LC 49 — Group Anagrams](https://leetcode.com/problems/group-anagrams/) — HashMap по каноническому ключу.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [ACMP 82 — Пересечение множеств](https://acmp.ru/index.asp?main=task&id_task=82) | — | `D` | <details><summary>Показать после попытки</summary>Множество принадлежности и удаление дубликатов</details> |
| 2 | [CF 1703B — ICPC Balloons](https://codeforces.com/problemset/problem/1703/B) | 800 | `L` | HashSet для первого появления элемента |
| 3 | [CF 1722C — Word Game](https://codeforces.com/problemset/problem/1722/C) | 800 | `L` | HashMap частот строк между несколькими наборами |
| 4 | [CF 4C — Registration System](https://codeforces.com/problemset/problem/4/C) | 1300 | `L` | HashMap: чтение, проверка и обновление счётчика |
| 5 | [CF 1955B — Progressive Square](https://codeforces.com/problemset/problem/1955/B) | 1000 | `R` | Сравнение мультимножеств через частоты |
| 6 | [CF 1520D — Same Differences](https://codeforces.com/problemset/problem/1520/D) | 1200 | `R` | Подсчёт пар по преобразованному ключу |
| 7 | [CF 1791F — Range Update Point Query](https://codeforces.com/problemset/problem/1791/F) | 1500 | `H` | TreeSet.ceiling и удаление стабилизировавшихся индексов |
| 8 | [ACMP 816 — Система пересекающихся множеств](https://acmp.ru/index.asp?main=task&id_task=816) | — | `F` | <details><summary>Показать после попытки</summary>Двусторонние списки принадлежности множествам</details> |
| 9 | [CF 1108B — Divisors of Two Integers](https://codeforces.com/problemset/problem/1108/B) | 1100 | `X` | <details><summary>Показать после попытки</summary>Мультимножество делителей и восстановление двух объектов</details> |

## 5. Стек, очередь, дек и приоритетная очередь

Этап **A0**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 5](ROADMAP.md#тема-5).

База LeetCode, не входит в лимит: [LC 20 — Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) — Стек для корректной вложенности; [LC 239 — Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) — Монотонный дек для максимума окна.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [ACMP 899 — Баланс скобок](https://acmp.ru/index.asp?main=task&id_task=899) | — | `D` | <details><summary>Показать после попытки</summary>Стек для проверки корректной вложенности</details> |
| 2 | [ACMP 946 — Полка](https://acmp.ru/index.asp?main=task&id_task=946) | — | `L` | Дек с операциями на обоих концах |
| 3 | [CF 450A — Jzzhu and Children](https://codeforces.com/problemset/problem/450/A) | 1000 | `L` | Очередь и циклическая обработка состояний |
| 4 | [CF 1907B — YetnotherrokenKeoard](https://codeforces.com/problemset/problem/1907/B) | 1000 | `L` | Два стека индексов для отката символов |
| 5 | [CF 343B — Alternating Current](https://codeforces.com/problemset/problem/343/B) | 1600 | `R` | Стековая редукция соседних элементов |
| 6 | [CF 1579D — Productive Meeting](https://codeforces.com/problemset/problem/1579/D) | 1400 | `R` | Max-heap с повторным добавлением изменённых состояний |
| 7 | [CF 1353D — Constructing the Array](https://codeforces.com/problemset/problem/1353/D) | 1600 | `R` | PriorityQueue со строгим составным приоритетом |
| 8 | [CF 797C — Minimal string](https://codeforces.com/problemset/problem/797/C) | 1700 | `H` | Стек + минимум необработанного суффикса |
| 9 | [CF 1313C2 — Skyscrapers (hard version)](https://codeforces.com/problemset/problem/1313/C2) | 1900 | `F` | <details><summary>Показать после попытки</summary>Два монотонных стека и вклад каждого элемента</details> |
| 10 | [CF 5C — Longest Regular Bracket Sequence](https://codeforces.com/problemset/problem/5/C) | 1900 | `X` | <details><summary>Показать после попытки</summary>Стек или DP для максимальной правильной скобочной подстроки</details> |

Отдельная практика, не входит в лимит:

**Checkpoint монотонных структур, обязателен для A0.**

1. С нуля реализовать nearest smaller to the left через монотонный стек и проверить на массивах с дублями.
2. С нуля реализовать максимум каждого окна длины k через монотонный дек за O(n).
3. Письменно сформулировать, когда элементы удаляются с головы и с хвоста дека, и почему каждый индекс входит и выходит не более одного раза.

## 6. Префиксные суммы, разности, 2D-префиксы и sweep line

Этап **A1**. Задач: **11**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 6](ROADMAP.md#тема-6).

База LeetCode, не входит в лимит: [LC 303 — Range Sum Query — Immutable](https://leetcode.com/problems/range-sum-query-immutable/) — Одномерные префиксные суммы; [LC 304 — Range Sum Query 2D — Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) — Двумерные префиксные суммы.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [CF 1807D — Odd Queries](https://codeforces.com/problemset/problem/1807/D) | 900 | `D` | <details><summary>Показать после попытки</summary>Префиксная сумма и виртуальная замена подотрезка</details> |
| 2 | [CF 363B — Fence](https://codeforces.com/problemset/problem/363/B) | 1100 | `L` | Сумма фиксированного окна через префиксы |
| 3 | [CF 313B — Ilya and Queries](https://codeforces.com/problemset/problem/313/B) | 1100 | `L` | Префикс по локальному признаку соседней пары |
| 4 | [CF 433B — Kuriyama Mirai's Stones](https://codeforces.com/problemset/problem/433/B) | 1200 | `L` | Два массива префиксов для разных порядков |
| 5 | [CF 816B — Karen and Coffee](https://codeforces.com/problemset/problem/816/B) | 1400 | `R` | Difference array + второй префикс для запросов |
| 6 | [CF 276C — Little Girl and Maximum Sum](https://codeforces.com/problemset/problem/276/C) | 1500 | `R` | Разности частот запросов + перестановочный greedy |
| 7 | [CF 1722E — Counting Rectangles](https://codeforces.com/problemset/problem/1722/E) | 1600 | `R` | Двумерные префиксные суммы по таблице признаков |
| 8 | [CF 295A — Greg and Array](https://codeforces.com/problemset/problem/295/A) | 1400 | `R` | Два уровня difference arrays для диапазонов операций |
| 9 | [CF 1795C — Tea Tasting](https://codeforces.com/problemset/problem/1795/C) | 1500 | `H` | Бинарный поиск конца вклада + разностное накопление |
| 10 | [CF 466C — Number of Ways](https://codeforces.com/problemset/problem/466/C) | 1700 | `F` | <details><summary>Показать после попытки</summary>Префиксные счётчики подходящих точек разбиения</details> |
| 11 | [CF 1000C — Covered Points Count](https://codeforces.com/problemset/problem/1000/C) | 1700 | `X` | <details><summary>Показать после попытки</summary>Sweep line и порядок событий на равных координатах</details> |

## 7. Два указателя и скользящее окно

Этап **A1**. Задач: **12**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 7](ROADMAP.md#тема-7).

База LeetCode, не входит в лимит: [LC 3 — Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) — Окно с частотами символов; [LC 11 — Container With Most Water](https://leetcode.com/problems/container-with-most-water/) — Встречные указатели.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [CF 279B — Books](https://codeforces.com/problemset/problem/279/B) | 1400 | `D` | <details><summary>Показать после попытки</summary>Максимальное окно с ограничением на сумму</details> |
| 2 | [CF 1690D — Black and White Stripe](https://codeforces.com/problemset/problem/1690/D) | 1000 | `L` | Фиксированное окно и число замен |
| 3 | [CF 1840C — Ski Resort](https://codeforces.com/problemset/problem/1840/C) | 1000 | `L` | Подсчёт всех окон внутри допустимых серий |
| 4 | [CF 2060C — Game of Mathletes](https://codeforces.com/problemset/problem/2060/C) | 900 | `L` | Встречные указатели после сортировки |
| 5 | [CF 1354B — Ternary String](https://codeforces.com/problemset/problem/1354/B) | 1200 | `L` | Последнее появление классов и минимальное покрывающее окно |
| 6 | [CF 1669F — Eating Candies](https://codeforces.com/problemset/problem/1669/F) | 1100 | `R` | Встречные указатели и равные накопленные суммы |
| 7 | [CF 489B — BerSU Ball](https://codeforces.com/problemset/problem/489/B) | 1200 | `R` | Жадное сопоставление двух отсортированных массивов |
| 8 | [CF 580B — Kefa and Company](https://codeforces.com/problemset/problem/580/B) | 1500 | `R` | Переменное окно после сортировки по ключу |
| 9 | [CF 224B — Array](https://codeforces.com/problemset/problem/224/B) | 1500 | `R` | Частотное окно с ровно k различными значениями |
| 10 | [ACMP 649 — Защищенный пароль](https://acmp.ru/index.asp?main=task&id_task=649) | — | `H` | Окно с частотами и подсчётом всех допустимых строк |
| 11 | [ACMP 245 — Сплоченная команда](https://acmp.ru/index.asp?main=task&id_task=245) | — | `F` | <details><summary>Показать после попытки</summary>Сортировка + окно допустимого диапазона + максимум суммы</details> |
| 12 | [CF 1358D — The Best Vacation](https://codeforces.com/problemset/problem/1358/D) | 1900 | `X` | <details><summary>Показать после попытки</summary>Циклическое взвешенное окно и частичный край</details> |

## 8. Бинарный/тернарный поиск и поиск по ответу

Этап **A1**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 8](ROADMAP.md#тема-8).

База LeetCode, не входит в лимит: [LC 704 — Binary Search](https://leetcode.com/problems/binary-search/) — Классический binary search; [LC 875 — Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) — Binary search on answer.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [ACMP 267 — Ксерокопии](https://acmp.ru/index.asp?main=task&id_task=267) | — | `D` | <details><summary>Показать после попытки</summary>First true: минимальное время производства</details> |
| 2 | [CF 706B — Interesting drink](https://codeforces.com/problemset/problem/706/B) | 1100 | `L` | Upper bound: число элементов не больше x |
| 3 | [CF 474B — Worms](https://codeforces.com/problemset/problem/474/B) | 1200 | `L` | Lower bound по монотонным префиксным границам |
| 4 | [CF 1352C — K-th Not Divisible by n](https://codeforces.com/problemset/problem/1352/C) | 1200 | `L` | Поиск k-го допустимого числа по монотонному счётчику |
| 5 | [CF 670D1 — Magic Powder - 1](https://codeforces.com/problemset/problem/670/D1) | 1400 | `R` | Binary search on answer + линейная can(x) |
| 6 | [CF 1873E — Building an Aquarium](https://codeforces.com/problemset/problem/1873/E) | 1100 | `R` | Поиск максимальной высоты при ограниченной стоимости |
| 7 | [ACMP 523 — Роман в томах](https://acmp.ru/index.asp?main=task&id_task=523) | — | `R` | Минимизация максимального блока через greedy can(x) |
| 8 | [CF 371C — Hamburgers](https://codeforces.com/problemset/problem/371/C) | 1600 | `H` | Поиск ответа с аккуратной верхней границей и long |
| 9 | [CF 1742E — Scuza](https://codeforces.com/problemset/problem/1742/E) | 1200 | `F` | <details><summary>Показать после попытки</summary>Upper bound по максимумам префикса + сумма префикса</details> |
| 10 | [CF 1355E — Restorer Distance](https://codeforces.com/problemset/problem/1355/E) | 2100 | `X` | <details><summary>Показать после попытки</summary>Дискретная унимодальность и тернарный поиск стоимости</details> |

## 9. Жадные алгоритмы, инварианты и обменный аргумент

Этап **A1**. Задач: **11**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 9](ROADMAP.md#тема-9).

База LeetCode, не входит в лимит: [LC 55 — Jump Game](https://leetcode.com/problems/jump-game/) — Greedy-инвариант дальней достижимой позиции; [LC 435 — Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) — Interval scheduling по правому концу.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [CF 34B — Sale](https://codeforces.com/problemset/problem/34/B) | 900 | `D` | <details><summary>Показать после попытки</summary>Выбор фиксированного числа наиболее выгодных элементов</details> |
| 2 | [CF 337A — Puzzles](https://codeforces.com/problemset/problem/337/A) | 900 | `L` | Минимальный диапазон после сортировки |
| 3 | [CF 514A — Chewbaсca and Number](https://codeforces.com/problemset/problem/514/A) | 1200 | `L` | Независимый локально оптимальный выбор |
| 4 | [CF 158B — Taxi](https://codeforces.com/problemset/problem/158/B) | 1100 | `L` | Жадная упаковка групп ограниченных размеров |
| 5 | [CF 545C — Woodcutters](https://codeforces.com/problemset/problem/545/C) | 1500 | `L` | Жадная обработка интервалов слева направо |
| 6 | [CF 545D — Queue](https://codeforces.com/problemset/problem/545/D) | 1300 | `R` | Scheduling: сортировка и инвариант принятого префикса |
| 7 | [CF 58A — Chat room](https://codeforces.com/problemset/problem/58/A) | 1000 | `R` | Жадное распознавание подпоследовательности |
| 8 | [CF 1041C — Coffee Break](https://codeforces.com/problemset/problem/1041/C) | 1600 | `R` | Жадное распределение событий через ordered set |
| 9 | [CF 853A — Planning](https://codeforces.com/problemset/problem/853/A) | 1500 | `H` | Priority queue и выбор максимальной текущей потери |
| 10 | [ACMP 39 — Волосатый бизнес](https://acmp.ru/index.asp?main=task&id_task=39) | — | `F` | <details><summary>Показать после попытки</summary>Суффиксный максимум и доказательство момента действия</details> |
| 11 | [CF 1365D — Solve The Maze](https://codeforces.com/problemset/problem/1365/D) | 1700 | `X` | <details><summary>Показать после попытки</summary>Локальное жадное блокирование + проверка достижимости</details> |

## 10. Биты, маски, подмаски и булева алгебра

Этап **A1**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 10](ROADMAP.md#тема-10).

База LeetCode, не входит в лимит: [LC 1239 — Maximum Length of a Concatenated String with Unique Characters](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/) — Битовая маска множества и проверка конфликтов; [LC 1310 — XOR Queries of a Subarray](https://leetcode.com/problems/xor-queries-of-a-subarray/) — Префиксный XOR.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [ACMP 542 — Бит-реверс](https://acmp.ru/index.asp?main=task&id_task=542) | — | `D` | <details><summary>Показать после попытки</summary>Извлечение битов и построение числа сдвигами</details> |
| 2 | [CF 579A — Raising Bacteria](https://codeforces.com/problemset/problem/579/A) | 1000 | `L` | Popcount как минимальное число степеней двойки |
| 3 | [CF 1559A — Mocha and Math](https://codeforces.com/problemset/problem/1559/A) | 900 | `L` | Сведение последовательности побитовым AND |
| 4 | [CF 467B — Fedor and New Game](https://codeforces.com/problemset/problem/467/B) | 1100 | `L` | XOR двух масок и popcount различий |
| 5 | [CF 1420B — Rock and Lever](https://codeforces.com/problemset/problem/1420/B) | 1200 | `R` | Группировка по старшему установленному биту |
| 6 | [CF 1362C — Johnny and Another Rating Drop](https://codeforces.com/problemset/problem/1362/C) | 1400 | `R` | Вклады младших битов при последовательном изменении числа |
| 7 | [CF 1095C — Powers Of Two](https://codeforces.com/problemset/problem/1095/C) | 1400 | `R` | Разбиение числа на степени двойки через heap/lowbit |
| 8 | [CF 1552D — Array Differentiation](https://codeforces.com/problemset/problem/1552/D) | 1800 | `H` | Явный перебор подмасок циклом sub=(sub-1)&mask |
| 9 | [CF 1516B — AGAGA XOOORRR](https://codeforces.com/problemset/problem/1516/B) | 1500 | `F` | <details><summary>Показать после попытки</summary>Префиксный XOR и разбиение на равные XOR-сегменты</details> |
| 10 | [CF 449D — Jzzhu and Numbers](https://codeforces.com/problemset/problem/449/D) | 2400 | `X` | <details><summary>Показать после попытки</summary>SOS DP по маскам + inclusion–exclusion</details> |

## 11. Теория чисел: gcd, простые, факторизация, решето

Этап **A1**. Задач: **13**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 11](ROADMAP.md#тема-11).

База LeetCode, не входит в лимит: [LC 204 — Count Primes](https://leetcode.com/problems/count-primes/) — Решето Эратосфена; [LC 1979 — Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) — Алгоритм Евклида.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [ACMP 14 — НОК](https://acmp.ru/index.asp?main=task&id_task=14) | — | `D` | <details><summary>Показать после попытки</summary>GCD/LCM и безопасный порядок умножения</details> |
| 2 | [CF 17A — Noldbach problem](https://codeforces.com/problemset/problem/17/A) | 1000 | `L` | Решето простых и проверка специального представления |
| 3 | [CF 230B — T-primes](https://codeforces.com/problemset/problem/230/B) | 1300 | `L` | Решето + проверка квадрата простого числа |
| 4 | [CF 546D — Soldier and Number Game](https://codeforces.com/problemset/problem/546/D) | 1700 | `L` | SPF-sieve и префикс числа простых множителей с кратностью |
| 5 | [CF 26A — Almost Prime](https://codeforces.com/problemset/problem/26/A) | 900 | `L` | Подсчёт различных простых делителей для всех чисел |
| 6 | [CF 1294C — Product of Three Numbers](https://codeforces.com/problemset/problem/1294/C) | 1300 | `L` | Пробное деление и выделение множителей за O(sqrt n) |
| 7 | [CF 762A — k-th divisor](https://codeforces.com/problemset/problem/762/A) | 1400 | `L` | Перечисление делителей за O(sqrt n) в возрастающем порядке |
| 8 | [CF 7C — Line](https://codeforces.com/problemset/problem/7/C) | 1800 | `R` | Extended gcd и линейное диофантово уравнение |
| 9 | [CF 1295D — Same GCDs](https://codeforces.com/problemset/problem/1295/D) | 1800 | `R` | Преобразование gcd-условия к функции Эйлера |
| 10 | [CF 687B — Remainders Game](https://codeforces.com/problemset/problem/687/B) | 1800 | `R` | CRT-интуиция: достаточность набора модулей через LCM |
| 11 | [CF 1627D — Not Adding](https://codeforces.com/problemset/problem/1627/D) | 1900 | `H` | Sieve-like обработка gcd по всем кратным |
| 12 | [CF 1500B — Two chandeliers](https://codeforces.com/problemset/problem/1500/B) | 2200 | `H` | Generalized CRT + gcd-совместимость + поиск по ответу |
| 13 | [CF 710D — Two Arithmetic Progressions](https://codeforces.com/problemset/problem/710/D) | 2500 | `X` | <details><summary>Показать после попытки</summary>Линейные сравнения и CRT для пересечения прогрессий</details> |

## 12. Модульная арифметика и комбинаторика

Этап **A1**. Задач: **11**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 12](ROADMAP.md#тема-12).

База LeetCode, не входит в лимит: [LC 62 — Unique Paths](https://leetcode.com/problems/unique-paths/) — Подсчёт путей: DP или сочетания; [LC 1641 — Count Sorted Vowel Strings](https://leetcode.com/problems/count-sorted-vowel-strings/) — Комбинации с повторениями.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [ACMP 158 — Великий комбинатор](https://acmp.ru/index.asp?main=task&id_task=158) | — | `D` | <details><summary>Показать после попытки</summary>Комбинаторная модель распределения с повторениями</details> |
| 2 | [CF 1514B — AND 0, Sum Big](https://codeforces.com/problemset/problem/1514/B) | 1200 | `L` | Быстрое возведение в степень по модулю |
| 3 | [CF 553A — Kyoya and Colored Balls](https://codeforces.com/problemset/problem/553/A) | 1500 | `L` | Последовательное применение сочетаний |
| 4 | [CF 459B — Pashmak and Flowers](https://codeforces.com/problemset/problem/459/B) | 1300 | `L` | Подсчёт пар экстремальных значений |
| 5 | [CF 478B — Random Teams](https://codeforces.com/problemset/problem/478/B) | 1300 | `R` | Экстремальное распределение и C(x,2) |
| 6 | [CF 1444B — Divide and Sum](https://codeforces.com/problemset/problem/1444/B) | 1900 | `R` | Factorial/invfactorial и центральный биномиальный коэффициент |
| 7 | [CF 1436C — Binary Search](https://codeforces.com/problemset/problem/1436/C) | 1500 | `R` | Комбинаторное моделирование пути binary search |
| 8 | [CF 300C — Beautiful Numbers](https://codeforces.com/problemset/problem/300/C) | 1800 | `R` | Factorial/invfactorial + перебор числа выбранных цифр |
| 9 | [CF 340E — Iahub and Permutations](https://codeforces.com/problemset/problem/340/E) | 2000 | `H` | Derangements и inclusion–exclusion |
| 10 | [CF 1305C — Kuroni and Impossible Calculation](https://codeforces.com/problemset/problem/1305/C) | 1600 | `F` | <details><summary>Показать после попытки</summary>Принцип Дирихле + произведение попарных разностей</details> |
| 11 | [CF 451E — Devu and Flowers](https://codeforces.com/problemset/problem/451/E) | 2300 | `X` | <details><summary>Показать после попытки</summary>Inclusion–exclusion по верхним ограничениям + сочетания</details> |

## 13. Строки: префикс-функция, Z-функция и хеширование

Этап **A1**. Задач: **9**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 13](ROADMAP.md#тема-13).

База LeetCode, не входит в лимит: [LC 28 — Find the Index of the First Occurrence](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) — Базовый поиск подстроки; [LC 214 — Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) — KMP и палиндромный префикс.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [ACMP 202 — Поиск подстроки](https://acmp.ru/index.asp?main=task&id_task=202) | — | `D` | <details><summary>Показать после попытки</summary>KMP/Z: поиск всех вхождений образца</details> |
| 2 | [ACMP 204 — Циклическая строка](https://acmp.ru/index.asp?main=task&id_task=204) | — | `L` | Граница строки и минимальный период |
| 3 | [CF 126B — Password](https://codeforces.com/problemset/problem/126/B) | 1700 | `L` | Дерево границ prefix=suffix и внутреннее вхождение |
| 4 | [CF 471D — MUH and Cube Walls](https://codeforces.com/problemset/problem/471/D) | 1800 | `R` | KMP/Z по массиву разностей |
| 5 | [CF 432D — Prefixes and Suffixes](https://codeforces.com/problemset/problem/432/D) | 2000 | `R` | Z-function и подсчёт вхождений всех границ |
| 6 | [CF 1200E — Compress Words](https://codeforces.com/problemset/problem/1200/E) | 2000 | `R` | Максимальное prefix/suffix перекрытие при последовательном слиянии |
| 7 | [CF 535D — Tavas and Malekas](https://codeforces.com/problemset/problem/535/D) | 1900 | `H` | Z-function для проверки совместимости перекрывающихся шаблонов |
| 8 | [CF 7D — Palindrome Degree](https://codeforces.com/problemset/problem/7/D) | 2200 | `F` | <details><summary>Показать после попытки</summary>Rolling hash + DP по палиндромным префиксам</details> |
| 9 | [CF 271D — Good Substrings](https://codeforces.com/problemset/problem/271/D) | 1800 | `X` | <details><summary>Показать после попытки</summary>Trie или rolling hash для различных подстрок с ограничением</details> |

Отдельная практика, не входит в лимит:

**Checkpoint базовых строковых функций, обязателен для A1.**

1. С нуля вычислить prefix function и Z-function для одной строки и сверить массивы на строках aaaaa, abacaba и abcababcab.
2. Решить один и тот же поиск всех вхождений двумя способами: KMP и Z-function через разделитель.
3. Реализовать двойной polynomial hash для сравнения подстрок и явно нормализовать границы полуинтервалов.

## 14. Обходы графа, компоненты, циклы и двудольность

Этап **A1**. Задач: **8**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 14](ROADMAP.md#тема-14).

База LeetCode, не входит в лимит: [LC 200 — Number of Islands](https://leetcode.com/problems/number-of-islands/) — Flood fill компонент; [LC 785 — Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) — Двудольная раскраска.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [CF 217A — Ice Skating](https://codeforces.com/problemset/problem/217/A) | 1200 | `D` | <details><summary>Показать после попытки</summary>Компоненты в неявно заданном графе</details> |
| 2 | [ACMP 99 — Лабиринт](https://acmp.ru/index.asp?main=task&id_task=99) | — | `L` | BFS в трёхмерном лабиринте |
| 3 | [CF 500A — New Year Transportation](https://codeforces.com/problemset/problem/500/A) | 1000 | `L` | Достижимость в функциональном ориентированном графе |
| 4 | [CF 510B — Fox And Two Dots](https://codeforces.com/problemset/problem/510/B) | 1500 | `L` | Цикл в неориентированной сетке с parent |
| 5 | [CF 1829E — The Lakes](https://codeforces.com/problemset/problem/1829/E) | 1100 | `R` | Flood fill компонент с агрегированием веса |
| 6 | [CF 687A — NP-Hard Problem](https://codeforces.com/problemset/problem/687/A) | 1500 | `R` | Двудольная раскраска общего графа |
| 7 | [CF 1702E — Split Into Two Sets](https://codeforces.com/problemset/problem/1702/E) | 1600 | `F` | <details><summary>Показать после попытки</summary>Степени + двудольность графа из пар</details> |
| 8 | [CF 377A — Maze](https://codeforces.com/problemset/problem/377/A) | 1600 | `X` | <details><summary>Показать после попытки</summary>DFS по сетке с сохранением связной части</details> |

## 15. Кратчайшие пути: BFS, 0–1 BFS, Дейкстра, Флойд, Беллман—Форд

Этап **A1**. Задач: **10**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 15](ROADMAP.md#тема-15).

База LeetCode, не входит в лимит: [LC 743 — Network Delay Time](https://leetcode.com/problems/network-delay-time/) — Dijkstra по списку рёбер; [LC 787 — Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) — DP/Bellman–Ford с ограничением числа рёбер.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [ACMP 132 — Алгоритм Дейкстры](https://acmp.ru/index.asp?main=task&id_task=132) | — | `D` | <details><summary>Показать после попытки</summary>Dijkstra: релаксация и выбор минимального расстояния</details> |
| 2 | [CF 520B — Two Buttons](https://codeforces.com/problemset/problem/520/B) | 1400 | `L` | BFS по неявному графу состояний |
| 3 | [CF 1063B — Labyrinth](https://codeforces.com/problemset/problem/1063/B) | 1800 | `L` | 0–1 BFS: стоимость горизонтального перехода |
| 4 | [ACMP 135 — Алгоритм Флойда](https://acmp.ru/index.asp?main=task&id_task=135) | — | `L` | Floyd–Warshall: все пары кратчайших путей |
| 5 | [ACMP 138 — Алгоритм Форда—Беллмана](https://acmp.ru/index.asp?main=task&id_task=138) | — | `R` | Bellman–Ford на графе с отрицательными рёбрами |
| 6 | [CF 938D — Buy a Ticket](https://codeforces.com/problemset/problem/938/D) | 2000 | `R` | Multi-source Dijkstra с разными начальными расстояниями |
| 7 | [CF 295B — Greg and Graph](https://codeforces.com/problemset/problem/295/B) | 1700 | `R` | Обратное добавление вершин во Floyd |
| 8 | [ACMP 140 — Цикл отрицательного веса](https://acmp.ru/index.asp?main=task&id_task=140) | — | `H` | Обнаружение и восстановление отрицательного цикла |
| 9 | [CF 20C — Dijkstra?](https://codeforces.com/problemset/problem/20/C) | 1900 | `F` | <details><summary>Показать после попытки</summary>Dijkstra + parent[] + восстановление пути</details> |
| 10 | [CF 449B — Jzzhu and Cities](https://codeforces.com/problemset/problem/449/B) | 2000 | `X` | <details><summary>Показать после попытки</summary>Dijkstra с несколькими типами стартовых рёбер</details> |

## 16. Деревья: Эйлеров обход, двоичные подъёмы и LCA

Этап **A1**. Задач: **12**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 16](ROADMAP.md#тема-16).

База LeetCode, не входит в лимит: [LC 236 — Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) — Lowest common ancestor; [LC 863 — All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) — Расстояния в дереве.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [ACMP 141 — Дерево](https://acmp.ru/index.asp?main=task&id_task=141) | — | `D` | <details><summary>Показать после попытки</summary>Проверка структуры дерева</details> |
| 2 | [CF 115A — Party](https://codeforces.com/problemset/problem/115/A) | 900 | `L` | Родители, глубины и высота леса |
| 3 | [CF 1057A — Bmail Computer Network](https://codeforces.com/problemset/problem/1057/A) | 900 | `L` | Восстановление пути от вершины к корню по parent[] |
| 4 | [CF 1006E — Military Problem](https://codeforces.com/problemset/problem/1006/E) | 1600 | `L` | Euler/preorder flatten + размер поддерева |
| 5 | [CF 580C — Kefa and Park](https://codeforces.com/problemset/problem/580/C) | 1500 | `L` | Корневой DFS с состоянием на пути |
| 6 | [CF 1676G — White-Black Balanced Subtrees](https://codeforces.com/problemset/problem/1676/G) | 1300 | `R` | Агрегирование баланса по поддереву |
| 7 | [CF 191C — Fools and Roads](https://codeforces.com/problemset/problem/191/C) | 1900 | `R` | LCA + разности на дереве + postorder-накопление |
| 8 | [CF 1328E — Tree Queries](https://codeforces.com/problemset/problem/1328/E) | 1900 | `R` | Ancestor relation через tin/tout |
| 9 | [CF 1304E — 1-Trees and Queries](https://codeforces.com/problemset/problem/1304/E) | 2000 | `H` | LCA, расстояния и чётность маршрута с дополнительным ребром |
| 10 | [CF Gym 100091B — LCA Продолжение](https://codeforces.com/gym/100091/problem/B) · [регистрация/отправка](https://codeforces.com/gym/100091) | — | `H` | Online LCA: двоичные подъёмы при добавлении листьев |
| 11 | [CF 519E — A and B and Lecture Rooms](https://codeforces.com/problemset/problem/519/E) | 2100 | `F` | <details><summary>Показать после попытки</summary>Binary lifting + размеры частей дерева</details> |
| 12 | [CF 383C — Propagating tree](https://codeforces.com/problemset/problem/383/C) | 2000 | `X` | <details><summary>Показать после попытки</summary>Euler flatten + Fenwick с учётом чётности глубины</details> |

Отдельная практика, не входит в лимит:

**Checkpoint элементарных деревьев, обязателен до LCA.**

1. Одним postorder вычислить parent, depth и размер каждого поддерева.
2. Найти диаметр дерева двумя обходами и отдельно восстановить сам путь диаметра.
3. Построить таблицу binary lifting и проверить запросы k-го предка до перехода к LCA.

## 17. Базовое DP: пути, рюкзак, LIS и восстановление ответа

Этап **A1**. Задач: **13**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 17](ROADMAP.md#тема-17).

База LeetCode, не входит в лимит: [LC 322 — Coin Change](https://leetcode.com/problems/coin-change/) — Unbounded knapsack; [LC 300 — Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) — Longest increasing subsequence.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [ACMP 11 — Зайчик](https://acmp.ru/index.asp?main=task&id_task=11) | — | `D` | <details><summary>Показать после попытки</summary>Число способов и одномерная рекуррентность</details> |
| 2 | [ACMP 121 — Гвоздики](https://acmp.ru/index.asp?main=task&id_task=121) | — | `L` | Одномерное DP после сортировки |
| 3 | [CF 189A — Cut Ribbon](https://codeforces.com/problemset/problem/189/A) | 1300 | `L` | Unbounded knapsack на максимум числа предметов |
| 4 | [CF 698A — Vacations](https://codeforces.com/problemset/problem/698/A) | 1400 | `L` | Малое состояние предыдущего действия |
| 5 | [CF 474D — Flowers](https://codeforces.com/problemset/problem/474/D) | 1700 | `L` | Число способов набрать сумму переходами двух размеров |
| 6 | [CF 327A — Flipping Game](https://codeforces.com/problemset/problem/327/A) | 1200 | `L` | DP максимального подотрезка после преобразования выигрыша |
| 7 | [CF 1195C — Basketball Exercise](https://codeforces.com/problemset/problem/1195/C) | 1400 | `R` | Prefix DP с двумя рядами |
| 8 | [CF 455A — Boredom](https://codeforces.com/problemset/problem/455/A) | 1500 | `R` | Сжатие частот + choose/skip DP |
| 9 | [CF 4D — Mysterious Present](https://codeforces.com/problemset/problem/4/D) | 1700 | `R` | LIS-подобное DP + parent для восстановления |
| 10 | [CF 977F — Consecutive Subsequence](https://codeforces.com/problemset/problem/977/F) | 1700 | `R` | DP по значению с восстановлением индексов подпоследовательности |
| 11 | [CF 577B — Modulo Sum](https://codeforces.com/problemset/problem/577/B) | 1900 | `H` | 0/1 subset-sum DP по остаткам + pigeonhole |
| 12 | [CF 706C — Hard problem](https://codeforces.com/problemset/problem/706/C) | 1600 | `F` | <details><summary>Показать после попытки</summary>Два состояния строки, INF и переходы</details> |
| 13 | [CF 864E — Fire](https://codeforces.com/problemset/problem/864/E) | 2000 | `X` | <details><summary>Показать после попытки</summary>0/1 knapsack с дедлайнами и восстановлением набора</details> |

Отдельная практика, не входит в лимит:

**Checkpoint классического DP, обязателен для A1.**

1. Реализовать четыре независимых DP: grid paths с препятствиями, минимум монет, число способов набрать сумму и 0/1 knapsack.
2. Реализовать LCS и edit distance с полной таблицей, затем восстановить один оптимальный ответ.
3. Реализовать LIS сначала за O(n^2), затем за O(n log n), и сравнить результаты на случайных малых тестах.

## 18. Fenwick, segment tree, lazy propagation и sparse table

Этап **A1**. Задач: **12**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 18](ROADMAP.md#тема-18).

База LeetCode, не входит в лимит: [LC 307 — Range Sum Query — Mutable](https://leetcode.com/problems/range-sum-query-mutable/) — Изменяемые суммы диапазона; [LC 715 — Range Module](https://leetcode.com/problems/range-module/) — Динамическое множество интервалов.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [ACMP 1084 — Дерево Фенвика](https://acmp.ru/index.asp?main=task&id_task=1084) | — | `D` | <details><summary>Показать после попытки</summary>Fenwick: point update + range sum</details> |
| 2 | [ACMP 1185 — RMQ с изменением элемента](https://acmp.ru/index.asp?main=task&id_task=1185) | — | `L` | Базовое segment tree: point assignment + range maximum |
| 3 | [CF 459D — Pashmak and Parmida's problem](https://codeforces.com/problemset/problem/459/D) | 1800 | `L` | Offline-частоты + Fenwick |
| 4 | [CF 1208D — Restore Permutation](https://codeforces.com/problemset/problem/1208/D) | 1900 | `L` | Fenwick prefix lower-bound для восстановления перестановки |
| 5 | [CF 380C — Sereja and Brackets](https://codeforces.com/problemset/problem/380/C) | 2000 | `R` | Segment tree: собственный узел и ассоциативный merge |
| 6 | [CF 474F — Ant colony](https://codeforces.com/problemset/problem/474/F) | 2100 | `R` | Sparse table для GCD + частоты минимума |
| 7 | [CF 52C — Circular RMQ](https://codeforces.com/problemset/problem/52/C) | 2200 | `R` | Lazy range add/range min + циклический диапазон |
| 8 | [CF 1709D — Rorororobot](https://codeforces.com/problemset/problem/1709/D) | 1700 | `R` | Static RMQ maximum + арифметическая достижимость |
| 9 | [CF 1354D — Multiset](https://codeforces.com/problemset/problem/1354/D) | 1900 | `R` | Fenwick по частотам + поиск k-го элемента |
| 10 | [CF 242E — XOR on Segment](https://codeforces.com/problemset/problem/242/E) | 2000 | `H` | Lazy propagation по битам для range xor/range sum |
| 11 | [CF 438D — The Child and Sequence](https://codeforces.com/problemset/problem/438/D) | 2300 | `F` | <details><summary>Показать после попытки</summary>Segment tree с отсечением по максимуму для операции modulo</details> |
| 12 | [CF 61E — Enemy is weak](https://codeforces.com/problemset/problem/61/E) | 1900 | `X` | <details><summary>Показать после попытки</summary>Сжатие координат + два Fenwick для подсчёта троек</details> |

Отдельная практика, не входит в лимит:

**Checkpoint структуры запросов без олимпиадной надстройки.**

1. На одном интерфейсе запросов реализовать static range sum, static RMQ, Fenwick point-add/range-sum и segment tree point-set/range-min.
2. Сравнить все структуры с наивным массивом на случайных малых тестах.
3. Только после успешной сверки перейти к lazy propagation и нестандартным узлам segment tree.

## 19. Вычислительная геометрия

Этап **B**. Задач: **7**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 19](ROADMAP.md#тема-19).

База LeetCode, не входит в лимит: [LC 973 — K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) — Расстояния и выбор k объектов; [LC 149 — Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/) — Коллинеарность и нормализация направления.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [ACMP 348 — Пересечение отрезков](https://acmp.ru/index.asp?main=task&id_task=348) | — | `D` | <details><summary>Показать после попытки</summary>Orientation + point-on-segment + пересечение отрезков</details> |
| 2 | [ACMP 370 — Площадь многоугольника](https://acmp.ru/index.asp?main=task&id_task=370) | — | `L` | Площадь многоугольника через shoelace/cross product |
| 3 | [CF 772B — Volatile Kite](https://codeforces.com/problemset/problem/772/B) | 1800 | `L` | Расстояние от точки до прямой через cross product |
| 4 | [CF 993A — Two Squares](https://codeforces.com/problemset/problem/993/A) | 1600 | `R` | Пересечения сторон + containment выпуклых фигур |
| 5 | [ACMP 374 — Выпуклая оболочка — 2](https://acmp.ru/index.asp?main=task&id_task=374) | — | `H` | Выпуклая оболочка и обработка коллинеарных точек |
| 6 | [CF 166B — Polygons](https://codeforces.com/problemset/problem/166/B) | 2100 | `F` | <details><summary>Показать после попытки</summary>Строгое попадание выпуклого многоугольника без касаний</details> |
| 7 | [CF Gym 101554D — Robert Hood](https://codeforces.com/gym/101554/problem/D) · [регистрация/отправка](https://codeforces.com/gym/101554) | — | `X` | <details><summary>Показать после попытки</summary>Convex hull + rotating calipers для диаметра множества</details> |

## 20. DAG, топосортировка, SCC, мосты и точки сочленения

Этап **B**. Задач: **9**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 20](ROADMAP.md#тема-20).

База LeetCode, не входит в лимит: [LC 1192 — Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) — Мосты через tin/low; [LC 802 — Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/) — Состояния вершин ориентированного графа.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [CF 510C — Fox And Names](https://codeforces.com/problemset/problem/510/C) | 1600 | `D` | <details><summary>Показать после попытки</summary>Топологическая сортировка + невозможный префикс строк</details> |
| 2 | [CF 919D — Substring](https://codeforces.com/problemset/problem/919/D) | 1700 | `L` | Topological order + DAG DP |
| 3 | [CF 427C — Checkposts](https://codeforces.com/problemset/problem/427/C) | 1700 | `L` | SCC + агрегирование минимума и числа вариантов |
| 4 | [CF 1217D — Coloring Edges](https://codeforces.com/problemset/problem/1217/D) | 2100 | `L` | Ориентированный цикл: DFS с цветами 0/1/2 и обратные рёбра |
| 5 | [CF Gym 100083D — Точки сочленения](https://codeforces.com/gym/100083/problem/D) · [регистрация/отправка](https://codeforces.com/gym/100083) | — | `R` | Точки сочленения через tin/low |
| 6 | [CF 915D — Almost Acyclic Graph](https://codeforces.com/problemset/problem/915/D) | 2200 | `R` | Ориентированный цикл и удаление одного ребра-кандидата |
| 7 | [CF 118E — Bertown roads](https://codeforces.com/problemset/problem/118/E) | 2000 | `H` | Bridges + ориентация рёбер DFS-порядком |
| 8 | [CF 1000E — We Need More Bosses](https://codeforces.com/problemset/problem/1000/E) | 2100 | `F` | <details><summary>Показать после попытки</summary>Мосты + сжатие 2-edge-connected components + диаметр</details> |
| 9 | [CF 652E — Pursuit For Artifacts](https://codeforces.com/problemset/problem/652/E) | 2300 | `X` | <details><summary>Показать после попытки</summary>Bridge tree + агрегат наличия специального ребра на пути</details> |

## 21. DSU, MST и офлайн-связность

Этап **B**. Задач: **7**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 21](ROADMAP.md#тема-21).

База LeetCode, не входит в лимит: [LC 1584 — Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) — Minimum spanning tree; [LC 721 — Accounts Merge](https://leetcode.com/problems/accounts-merge/) — DSU по общим ключам.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [ACMP 142 — Минимальный каркас](https://acmp.ru/index.asp?main=task&id_task=142) | — | `D` | <details><summary>Показать после попытки</summary>Минимальный остов: базовая реализация Kruskal</details> |
| 2 | [CF 1167C — News Distribution](https://codeforces.com/problemset/problem/1167/C) | 1400 | `L` | DSU: массовые union и размер компоненты |
| 3 | [CF 25D — Roads not only in Berland](https://codeforces.com/problemset/problem/25/D) | 1900 | `L` | DSU: лишние рёбра и соединение компонент |
| 4 | [CF 1213G — Path Queries](https://codeforces.com/problemset/problem/1213/G) | 1800 | `R` | Offline activation по весу + DSU metadata |
| 5 | [CF 566D — Restructuring Company](https://codeforces.com/problemset/problem/566/D) | 1900 | `H` | DSU-next для пропуска обработанных индексов диапазона |
| 6 | [CF 1245D — Shichikuji and Power Grid](https://codeforces.com/problemset/problem/1245/D) | 1900 | `F` | <details><summary>Показать после попытки</summary>Prim на дополненном графе + восстановление объектов</details> |
| 7 | [CF 160D — Edges in MST](https://codeforces.com/problemset/problem/160/D) | 2300 | `X` | <details><summary>Показать после попытки</summary>Kruskal по группам веса + bridges во временном графе</details> |

## 22. DP по отрезкам, решёткам, графам и деревьям

Этап **B**. Задач: **8**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 22](ROADMAP.md#тема-22).

База LeetCode, не входит в лимит: [LC 312 — Burst Balloons](https://leetcode.com/problems/burst-balloons/) — Interval DP; [LC 337 — House Robber III](https://leetcode.com/problems/house-robber-iii/) — Tree DP.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [CF 1528A — Parsa's Humongous Tree](https://codeforces.com/problemset/problem/1528/A) | 1600 | `D` | <details><summary>Показать после попытки</summary>Tree DP с двумя состояниями вершины</details> |
| 2 | [CF 1695C — Zero Path](https://codeforces.com/problemset/problem/1695/C) | 1700 | `L` | Grid DP по минимуму и максимуму достижимой суммы |
| 3 | [CF 607B — Zuma](https://codeforces.com/problemset/problem/607/B) | 1900 | `L` | Interval DP с удалением совпадающих концов |
| 4 | [CF 225C — Barcode](https://codeforces.com/problemset/problem/225/C) | 1700 | `L` | DP по префиксу колонок и длине одноцветного блока |
| 5 | [CF 1517D — Explorer Space](https://codeforces.com/problemset/problem/1517/D) | 1800 | `R` | Многослойный grid DP на точное число шагов |
| 6 | [CF 161D — Distance in Tree](https://codeforces.com/problemset/problem/161/D) | 1800 | `H` | Tree DP по расстояниям и объединение детей |
| 7 | [CF 721C — Journey](https://codeforces.com/problemset/problem/721/C) | 1800 | `F` | <details><summary>Показать после попытки</summary>DAG DP + parent + восстановление пути</details> |
| 8 | [CF 1092F — Tree with Maximum Cost](https://codeforces.com/problemset/problem/1092/F) | 1900 | `X` | <details><summary>Показать после попытки</summary>Rerooting: перенос взвешенной суммы по ребру</details> |

## 23. DP по подмножествам, цифрам и профилю

Этап **B**. Задач: **7**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 23](ROADMAP.md#тема-23).

База LeetCode, не входит в лимит: [LC 464 — Can I Win](https://leetcode.com/problems/can-i-win/) — Game DP по подмножествам; [LC 902 — Numbers At Most N Given Digit Set](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/) — Digit DP.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [CF 1036C — Classy Numbers](https://codeforces.com/problemset/problem/1036/C) | 1900 | `D` | <details><summary>Показать после попытки</summary>Digit DP: position/tight/started и ограничение числа цифр</details> |
| 2 | [CF 580D — Kefa and Dishes](https://codeforces.com/problemset/problem/580/D) | 1800 | `L` | Subset DP: dp[mask][last] |
| 3 | [CF 8C — Looking for Order](https://codeforces.com/problemset/problem/8/C) | 2000 | `L` | Subset DP по парам + восстановление ответа |
| 4 | [CF 165E — Compatible Numbers](https://codeforces.com/problemset/problem/165/E) | 2200 | `R` | SOS DP по подмаскам для совместимой маски |
| 5 | [CF 1391D — 505](https://codeforces.com/problemset/problem/1391/D) | 2000 | `H` | Profile DP по маскам соседних столбцов |
| 6 | [CF 628D — Magic Numbers](https://codeforces.com/problemset/problem/628/D) | 2200 | `F` | <details><summary>Показать после попытки</summary>Digit DP с tight, modulo и позиционным ограничением</details> |
| 7 | [CF 55D — Beautiful numbers](https://codeforces.com/problemset/problem/55/D) | 2500 | `X` | <details><summary>Показать после попытки</summary>Digit DP с состоянием LCM ненулевых цифр</details> |

## 24. Декартово дерево, treap и порядковые структуры

Этап **B**. Задач: **6**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 24](ROADMAP.md#тема-24).

База LeetCode, не входит в лимит: [LC 315 — Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) — Order statistics/Fenwick; [LC 327 — Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/) — Prefix sums + merge-sort counting.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [CF Gym 102787E — Sneetches and Speeches 2](https://codeforces.com/gym/102787/problem/E) | — | `L` | Implicit treap: lazy flip/reverse и агрегаты непрерывного блока |
| 2 | [CF Gym 102787A — Shandom Ruffle](https://codeforces.com/gym/102787/problem/A) | — | `L` | Implicit treap: split/merge и перестановка блоков |
| 3 | [CF 706D — Vasiliy's Multiset](https://codeforces.com/problemset/problem/706/D) | 1800 | `R` | Bitwise trie: insert/erase/max XOR |
| 4 | [CF Gym 102787B — Pear TreaP](https://codeforces.com/gym/102787/problem/B) | — | `H` | Implicit treap + динамическая строка + двусторонние хеши |
| 5 | [CF 702F — T-Shirts](https://codeforces.com/problemset/problem/702/F) | 2800 | `F` | <details><summary>Показать после попытки</summary>Treap/BST с агрегатами и lazy-изменениями</details> |
| 6 | [CF 1748E — Yet Another Array Counting Problem](https://codeforces.com/problemset/problem/1748/E) | 2300 | `X` | <details><summary>Показать после попытки</summary>Cartesian tree + DP по поддеревьям</details> |

## 25. Потоки и паросочетания

Этап **B**. Задач: **7**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 25](ROADMAP.md#тема-25).

База LeetCode, не входит в лимит: [LC 1820 — Maximum Number of Accepted Invitations](https://leetcode.com/problems/maximum-number-of-accepted-invitations/) — Kuhn bipartite matching; [LC 1066 — Campus Bikes II](https://leetcode.com/problems/campus-bikes-ii/) — Assignment DP по маскам.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [CF 120H — Brevity is Soul of Wit](https://codeforces.com/problemset/problem/120/H) | 1800 | `D` | <details><summary>Показать после попытки</summary>Двудольная модель и увеличивающие пути Куна</details> |
| 2 | [CF 1423B — Valuable Paper](https://codeforces.com/problemset/problem/1423/B) | 1900 | `L` | Hopcroft–Karp + binary search по допустимому порогу |
| 3 | [CF 546E — Soldier and Traveling](https://codeforces.com/problemset/problem/546/E) | 2100 | `L` | Dinic и восстановление матрицы назначений |
| 4 | [CF 1666L — Labyrinth](https://codeforces.com/problemset/problem/1666/L) | 1800 | `R` | Два внутренне вершинно непересекающихся ориентированных пути |
| 5 | [CF 237E — Build String](https://codeforces.com/problemset/problem/237/E) | 2000 | `H` | Min-cost max-flow: ограниченные ресурсы и цена единицы потока |
| 6 | [CF 510E — Fox And Dinner](https://codeforces.com/problemset/problem/510/E) | 2300 | `F` | <details><summary>Показать после попытки</summary>Flow/matching + восстановление циклов</details> |
| 7 | [CF 1082G — Petya and Graph](https://codeforces.com/problemset/problem/1082/G) | 2400 | `X` | <details><summary>Показать после попытки</summary>Maximum closure как min-cut</details> |

## 26. Ахо—Корасик, Манакер, suffix array/automaton

Этап **B**. Задач: **8**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 26](ROADMAP.md#тема-26).

База LeetCode, не входит в лимит: [LC 1044 — Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/) — Двоичный поиск + rolling hash/suffix structure; [LC 336 — Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/) — Trie/hash для палиндромных пар.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [ACMP 70 — Степень строки](https://acmp.ru/index.asp?main=task&id_task=70) | — | `D` | <details><summary>Показать после попытки</summary>Границы и период строки как база suffix-структур</details> |
| 2 | [CF 1202E — You Are Given Some Strings...](https://codeforces.com/problemset/problem/1202/E) | 2400 | `L` | Aho–Corasick и агрегация совпадений |
| 3 | [CF 1326D2 — Prefix-Suffix Palindrome (Hard version)](https://codeforces.com/problemset/problem/1326/D2) | 1800 | `L` | Manacher для палиндрома после общего prefix/suffix |
| 4 | [CF 514C — Watto and Mechanism](https://codeforces.com/problemset/problem/514/C) | 2000 | `L` | Trie с одним допустимым несовпадением |
| 5 | [CF 19C — Deletion of Repeats](https://codeforces.com/problemset/problem/19/C) | 2200 | `R` | Suffix array/LCP для поиска повторяющихся блоков |
| 6 | [CF 123D — String](https://codeforces.com/problemset/problem/123/D) | 2300 | `H` | Suffix array + LCP + монотонная агрегация |
| 7 | [CF 710F — String Set Queries](https://codeforces.com/problemset/problem/710/F) | 2400 | `F` | <details><summary>Показать после попытки</summary>Динамический набор Aho–Corasick через логарифмические объединения</details> |
| 8 | [CF 873F — Forbidden Indices](https://codeforces.com/problemset/problem/873/F) | 2400 | `X` | <details><summary>Показать после попытки</summary>Suffix automaton + агрегация по suffix links</details> |

## 27. HLD, центроидная декомпозиция, small-to-large и rerooting

Этап **B**. Задач: **7**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 27](ROADMAP.md#тема-27).

База LeetCode, не входит в лимит: [LC 834 — Sum of Distances in Tree](https://leetcode.com/problems/sum-of-distances-in-tree/) — Rerooting; [LC 1483 — Kth Ancestor of a Tree Node](https://leetcode.com/problems/kth-ancestor-of-a-tree-node/) — Binary lifting.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [CF 1324F — Maximum White Subtree](https://codeforces.com/problemset/problem/1324/F) | 1800 | `D` | <details><summary>Показать после попытки</summary>Базовый rerooting с переносом лучшей суммы</details> |
| 2 | [CF 1187E — Tree Painting](https://codeforces.com/problemset/problem/1187/E) | 2100 | `L` | Rerooting с переносом ответа по ребру |
| 3 | [CF 321C — Ciel the Commander](https://codeforces.com/problemset/problem/321/C) | 2100 | `L` | Построение centroid decomposition |
| 4 | [CF 600E — Lomsat gelral](https://codeforces.com/problemset/problem/600/E) | 2300 | `R` | DSU-on-tree/small-to-large по частотам цветов |
| 5 | [CF 593D — Happy Tree Party](https://codeforces.com/problemset/problem/593/D) | 2400 | `H` | HLD + segment tree на путях |
| 6 | [CF 342E — Xenia and Tree](https://codeforces.com/problemset/problem/342/E) | 2400 | `F` | <details><summary>Показать после попытки</summary>Centroid decomposition для динамического множества</details> |
| 7 | [CF 375D — Tree and Queries](https://codeforces.com/problemset/problem/375/D) | 2400 | `X` | <details><summary>Показать после попытки</summary>DSU-on-tree по частотам цветов в поддеревьях</details> |

## 28. Теория игр: выигрыш/проигрыш, Nim и Sprague—Grundy

Этап **B**. Задач: **7**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 28](ROADMAP.md#тема-28).

База LeetCode, не входит в лимит: [LC 292 — Nim Game](https://leetcode.com/problems/nim-game/) — Nim-инвариант; [LC 486 — Predict the Winner](https://leetcode.com/problems/predict-the-winner/) — Minimax/game DP.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [CF 1527B1 — Palindrome Game (easy version)](https://codeforces.com/problemset/problem/1527/B1) | 1200 | `D` | <details><summary>Показать после попытки</summary>Формальная классификация win/lose по инварианту состояния</details> |
| 2 | [CF 1033C — Permutation Game](https://codeforces.com/problemset/problem/1033/C) | 1600 | `L` | Win/lose DP на DAG состояний |
| 3 | [CF 15C — Industrial Nim](https://codeforces.com/problemset/problem/15/C) | 2000 | `L` | Nim и xor-sum куч, заданных диапазонами |
| 4 | [CF 455B — A Lot of Games](https://codeforces.com/problemset/problem/455/B) | 1900 | `R` | Два win/lose-состояния на trie |
| 5 | [CF 786A — Berzerk](https://codeforces.com/problemset/problem/786/A) | 2000 | `H` | Retrograde-анализ Win/Lose/Loop в циклическом графе |
| 6 | [CF 768E — Game of Stones](https://codeforces.com/problemset/problem/768/E) | 2100 | `F` | <details><summary>Показать после попытки</summary>Sprague–Grundy, mex и XOR независимых компонент</details> |
| 7 | [CF 850C — Arpa and a game with Mojtaba](https://codeforces.com/problemset/problem/850/C) | 2200 | `X` | <details><summary>Показать после попытки</summary>Sprague–Grundy по маскам степеней простых</details> |

## 29. Meet-in-the-middle и разбиение пространства поиска

Этап **B**. Задач: **7**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 29](ROADMAP.md#тема-29).

База LeetCode, не входит в лимит: [LC 1755 — Closest Subsequence Sum](https://leetcode.com/problems/closest-subsequence-sum/) — Meet-in-the-middle subset sums.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [CF 888E — Maximum Subsequence](https://codeforces.com/problemset/problem/888/E) | 1800 | `D` | <details><summary>Показать после попытки</summary>Две половины subset sums + поиск дополнения</details> |
| 2 | [CF 1006F — Xor-Paths](https://codeforces.com/problemset/problem/1006/F) | 2100 | `L` | Meet-in-the-middle по средней диагонали пути |
| 3 | [CF 525E — Anya and Cubes](https://codeforces.com/problemset/problem/525/E) | 2100 | `L` | Троичный перебор половин + подсчёт дополнений |
| 4 | [CF 1105E — Helping Hiasat](https://codeforces.com/problemset/problem/1105/E) | 2200 | `R` | MITM для maximum independent set при n≈40 |
| 5 | [CF 912E — Prime Gift](https://codeforces.com/problemset/problem/912/E) | 2400 | `H` | MITM по группам простых + поиск k-го произведения |
| 6 | [CF 585D — Lizard Era: Beginning](https://codeforces.com/problemset/problem/585/D) | 2300 | `F` | <details><summary>Показать после попытки</summary>MITM с восстановлением выбранных решений</details> |
| 7 | [CF 1257F — Make Them Similar](https://codeforces.com/problemset/problem/1257/F) | 2400 | `X` | <details><summary>Показать после попытки</summary>Разбиение пространства битов + hash векторов расстояний</details> |

## 30. Корневая декомпозиция, Mo и офлайн-запросы

Этап **C**. Задач: **5**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 30](ROADMAP.md#тема-30).

База LeetCode, не входит в лимит: [LC 493 — Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) — Подсчёт пар через merge sort.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [CF 220B — Little Elephant and Array](https://codeforces.com/problemset/problem/220/B) | 1800 | `L` | Mo: add/remove и частотный инвариант freq[x]=x |
| 2 | [CF 86D — Powerful array](https://codeforces.com/problemset/problem/86/D) | 2200 | `R` | Mo с нелинейным вкладом значения |
| 3 | [CF 617E — XOR and Favorite Number](https://codeforces.com/problemset/problem/617/E) | 2200 | `H` | Mo по массиву prefix XOR |
| 4 | [CF 13E — Holes](https://codeforces.com/problemset/problem/13/E) | 2700 | `F` | <details><summary>Показать после попытки</summary>Sqrt decomposition с point updates и jump-агрегатами</details> |
| 5 | [CF 455D — Serega and Fun](https://codeforces.com/problemset/problem/455/D) | 2700 | `X` | <details><summary>Показать после попытки</summary>Динамическая последовательность в блоках + частоты</details> |

## 31. Rollback, персистентность и динамическая связность

Этап **C**. Задач: **5**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 31](ROADMAP.md#тема-31).

База LeetCode, не входит в лимит: [LC 1146 — Snapshot Array](https://leetcode.com/problems/snapshot-array/) — Версии состояния массива.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [CF 707D — Persistent Bookcase](https://codeforces.com/problemset/problem/707/D) | 2200 | `L` | Дерево версий + DFS + ручной rollback изменений |
| 2 | [CF 813E — Army Creation](https://codeforces.com/problemset/problem/813/E) | 2200 | `R` | Persistent segment tree по предыдущим вхождениям |
| 3 | [CF 891C — Envy](https://codeforces.com/problemset/problem/891/C) | 2300 | `H` | Rollback DSU внутри групп одинакового веса |
| 4 | [CF 1140F — Extending Set of Points](https://codeforces.com/problemset/problem/1140/F) | 2600 | `F` | <details><summary>Показать после попытки</summary>Segment tree over time + rollback DSU</details> |
| 5 | [CF 484E — Sign on Fence](https://codeforces.com/problemset/problem/484/E) | 2500 | `X` | <details><summary>Показать после попытки</summary>Версии persistent segment tree по порогу</details> |

## 32. Оптимизации DP: CHT/Li Chao, divide-and-conquer, Knuth

Этап **C**. Задач: **5**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 32](ROADMAP.md#тема-32).

База LeetCode, не входит в лимит: [LC 410 — Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) — DP разбиений и поиск по ответу.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [CF 319C — Kalila and Dimna in the Logging Industry](https://codeforces.com/problemset/problem/319/C) | 2100 | `L` | Monotone CHT для линейного перехода DP |
| 2 | [CF 660F — Bear and Bowling 4](https://codeforces.com/problemset/problem/660/F) | 2500 | `R` | Li Chao Tree для запросов в немонотонных координатах |
| 3 | [CF 868F — Yet Another Minimization Problem](https://codeforces.com/problemset/problem/868/F) | 2500 | `H` | Divide-and-conquer optimization с подвижной стоимостью |
| 4 | [CF Gym 100212C — Order-Preserving Codes](https://codeforces.com/gym/100212/attachments/download/1727/20042005-winter-petrozavodsk-camp-andrew-stankevich-contest-10-en.pdf#page=4) · [регистрация/отправка](https://codeforces.com/gym/100212) | — | `F` | <details><summary>Показать после попытки</summary>Knuth optimization и границы оптимального разбиения</details> |
| 5 | [CF 932F — Escape Through Leaf](https://codeforces.com/problemset/problem/932/F) | 2700 | `X` | <details><summary>Показать после попытки</summary>Tree DP + Li Chao/small-to-large</details> |

## 33. Матрицы, линейная алгебра, FFT/NTT

Этап **C**. Задач: **5**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 33](ROADMAP.md#тема-33).

База LeetCode, не входит в лимит: [LC 509 — Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) — Линейная рекуррентность; [LC 43 — Multiply Strings](https://leetcode.com/problems/multiply-strings/) — Умножение больших чисел как база convolution.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [CF 222E — Decoding Genome](https://codeforces.com/problemset/problem/222/E) | 1900 | `L` | Матричное возведение автомата переходов |
| 2 | [ACMP 198 — Система линейных уравнений](https://acmp.ru/index.asp?main=task&id_task=198) | — | `R` | Плотный метод Гаусса с выбором ведущего элемента |
| 3 | [CF 1101G — (Zero XOR Subset)-less](https://codeforces.com/problemset/problem/1101/G) | 2300 | `H` | XOR basis как Gauss над GF(2) |
| 4 | [CF 1096G — Lucky Tickets](https://codeforces.com/problemset/problem/1096/G) | 2400 | `F` | <details><summary>Показать после попытки</summary>Polynomial exponentiation через FFT/NTT</details> |
| 5 | [CF 528D — Fuzzy Search](https://codeforces.com/problemset/problem/528/D) | 2500 | `X` | <details><summary>Показать после попытки</summary>Несколько convolution для неточного сопоставления строк</details> |

## 34. Вероятность, рандомизация, interactive и output-only

Этап **C**. Задач: **5**. Связь с этапом и признаки распознавания: [ROADMAP.md — тема 34](ROADMAP.md#тема-34).

База LeetCode, не входит в лимит: [LC 528 — Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/) — Случайный выбор по префиксным весам.

| № | Задача | Рейтинг CF | Роль | Что тренирует |
|---:|---|---:|:---:|---|
| 1 | [CF 839C — Journey](https://codeforces.com/problemset/problem/839/C) | 1500 | `L` | Линейность ожидания и вероятностный DFS на дереве |
| 2 | [CF 453A — Little Pony and Expected Maximum](https://codeforces.com/problemset/problem/453/A) | 1600 | `R` | Ожидание максимума через CDF/tail probabilities |
| 3 | [CF 869E — The Untended Antiquity](https://codeforces.com/problemset/problem/869/E) | 2400 | `H` | Randomized hashing множества активных прямоугольников |
| 4 | [CF 148D — Bag of mice](https://codeforces.com/problemset/problem/148/D) | 1800 | `F` | <details><summary>Показать после попытки</summary>Probability DP по состояниям количества объектов</details> |
| 5 | [CF 1114E — Arithmetic Progression](https://codeforces.com/problemset/problem/1114/E) | 2200 | `X` | <details><summary>Показать после попытки</summary>Randomized sampling внутри interactive-протокола</details> |

Отдельная практика, не входит в лимит:

**Практика с [официальным пакетом условий и checkers МОШ 2025/26](contests/14-moscow/2025-2026/final/full-with-answers-checkers.zip).**

1. Внутри архива выбрать A, C или E; точные пути: `10-11 Очный тур/<буква>/statements/.pdf/russian/problem.pdf` и `10-11 Очный тур/<буква>/check.cpp`.
2. Построить любое валидное решение.
3. Проверить его локально.
4. Улучшать score только после получения корректного решения.
