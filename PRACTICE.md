# Банк задач

Этот каталог построен под календарь `лето -> отборы в октябре-ноябре -> финалы в марте-апреле`. Внутри каждой темы
задачи уже расположены в учебном порядке: от первого знакомства с приемом до более сложного переноса идеи.

## Объём и маршрут

- этап A0: **38 Core** и **24 Extra** - инженерная и алгоритмическая база;
- этап A1: **96 Core** и **90 Extra** - основные переносимые олимпиадные паттерны;
- этап B: **60 Core** и **43 Extra** - регулярный финальный слой;
- этап C: **24 Core** и **9 Extra** - выборочная продвинутая практика;
- полный каталог: **218 Core** и **166 Extra**, всего **384** строки;
- онлайн-задачи: **373**, включая **66** задач LeetCode;
- локальные checkpoints: **11**, они входят в Core, но не являются задачами онлайн-судьи.

`Core` - основной маршрут: эти задачи нужно решить все и по порядку. Если задача уже знакома, ее все равно полезно
быстро перерешать и восстановить реализацию без старого кода. `Extra` - расширение темы после Core: его брать по
обнаруженным пробелам, для дополнительного закрепления или после прохождения отборов.

LeetCode больше не вынесен в отдельный абзац: вводные задачи стоят первыми прямо в таблице. Локальный checkpoint тоже
является обычным шагом маршрута и расположен там, где уже пора собрать реализацию целиком.

Колонка **`Паттерн`** описывает целевой учебный способ решения, а не утверждает, что других решений не существует.
Она специально оставлена видимой как карта навыков. Перед первой попыткой можно закрыть эту колонку, если хочется
сначала самостоятельно распознать прием по условию.

## Правила работы

1. Прочитать краткое объяснение темы и признаки распознавания в ROADMAP.
2. Решить все строки `Core` сверху вниз. Не пропускать LeetCode и локальные checkpoints только потому, что они не
   относятся к Codeforces.
3. Если задача дала переносимый вывод, записать его одной короткой строкой в [`NOTES.md`](NOTES.md). Для обычного
   решения без нового вывода заметка не нужна.
4. После Core перейти к следующей теме. `Extra` решать при заметном пробеле, для повторения или в финальном цикле.
5. ACMP используется как русскоязычный вход и тренировка реализации; Codeforces - как основная шкала сложности.
6. `LC Easy/Medium/Hard` показывает сложность LeetCode, `CF 1600` - рейтинг Codeforces, `-` - единой сопоставимой
   оценки нет. Сложность остается ориентиром: учебный порядок и целевой паттерн важнее одного числа.

<a id="practice-complexity-java"></a>

## 1. Оценка сложности, Java и аккуратная реализация

Этап **A0**. Core: **7**. Extra: **6**. Теория и признаки распознавания: [ROADMAP: сложность и Java](ROADMAP.md#topic-complexity-java).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 412 - Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) | LC Easy | Условия и форматирование вывода |
| 2 | `Core` | [LC 66 - Plus One](https://leetcode.com/problems/plus-one/) | LC Easy | Перенос разряда в массиве цифр |
| 3 | `Core` | [ACMP 1 - A+B](https://acmp.ru/index.asp?main=task&id_task=1) | - | Java: запуск решения и базовый ввод/вывод |
| 4 | `Core` | [CF 1A - Theatre Square](https://codeforces.com/problemset/problem/1/A) | CF 1000 | Потолочное деление и обязательный long при произведении |
| 5 | `Core` | [ACMP 5 - Статистика](https://acmp.ru/index.asp?main=task&id_task=5) | - | Массивы, фильтрация и точный формат вывода |
| 6 | `Core` | [CF 118A - String Task](https://codeforces.com/problemset/problem/118/A) | CF 1000 | Линейная фильтрация строки без лишних объектов |
| 7 | `Core` | Локальный checkpoint: надежность Java | Checkpoint | Оценить время и память; написать быстрый ввод; проверить long, comparator, StringBuilder и глубокий DFS |
| 8 | `Extra` | [CF 71A - Way Too Long Words](https://codeforces.com/problemset/problem/71/A) | CF 800 | Пакетный ввод строк и аккуратная обработка длины |
| 9 | `Extra` | [CF 282A - Bit++](https://codeforces.com/problemset/problem/282/A) | CF 800 | Разбор коротких команд и изменение счётчика |
| 10 | `Extra` | [CF 158A - Next Round](https://codeforces.com/problemset/problem/158/A) | CF 800 | Граница массива при равных значениях |
| 11 | `Extra` | [CF 263A - Beautiful Matrix](https://codeforces.com/problemset/problem/263/A) | CF 800 | Двумерная индексация и расстояние по координатам |
| 12 | `Extra` | [CF 492B - Vanya and Lanterns](https://codeforces.com/problemset/problem/492/B) | CF 1200 | Сортировка, граничные случаи и вещественная точность |
| 13 | `Extra` | [CF 112A - Petya and Strings](https://codeforces.com/problemset/problem/112/A) | CF 800 | Нормализация регистра и лексикографическое сравнение |

<a id="practice-bruteforce"></a>

## 2. Полный перебор, рекурсия и отсечения

Этап **A0**. Core: **6**. Extra: **6**. Теория и признаки распознавания: [ROADMAP: перебор](ROADMAP.md#topic-bruteforce).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 46 - Permutations](https://leetcode.com/problems/permutations/) | LC Medium | Backtracking перестановок |
| 2 | `Core` | [LC 78 - Subsets](https://leetcode.com/problems/subsets/) | LC Medium | Генерация всех подмножеств |
| 3 | `Core` | [CF 214A - System of Equations](https://codeforces.com/problemset/problem/214/A) | CF 800 | Полный перебор двух переменных по малым ограничениям |
| 4 | `Core` | [CF 1097B - Petr and a Combination Lock](https://codeforces.com/problemset/problem/1097/B) | CF 1200 | Перебор 2^n вариантов выбора знака |
| 5 | `Core` | [CF 1950D - Product of Binary Decimals](https://codeforces.com/problemset/problem/1950/D) | CF 1100 | Рекурсивный перебор переходов с memoization |
| 6 | `Core` | [ACMP 101 - Магараджа](https://acmp.ru/index.asp?main=task&id_task=101) | - | Backtracking с rollback атакованных линий и клеток |
| 7 | `Extra` | [CF 271A - Beautiful Year](https://codeforces.com/problemset/problem/271/A) | CF 800 | Последовательный перебор до первого допустимого объекта |
| 8 | `Extra` | [CF 122A - Lucky Division](https://codeforces.com/problemset/problem/122/A) | CF 1000 | Перебор небольшого заранее ограниченного семейства |
| 9 | `Extra` | [CF 479A - Expression](https://codeforces.com/problemset/problem/479/A) | CF 1000 | Перебор фиксированного числа вариантов формулы |
| 10 | `Extra` | [CF 1108C - Nice Garland](https://codeforces.com/problemset/problem/1108/C) | CF 1300 | Перебор перестановок малого алфавита |
| 11 | `Extra` | [CF 124B - Permutations](https://codeforces.com/problemset/problem/124/B) | CF 1400 | Полный перебор n! перестановок |
| 12 | `Extra` | [CF 550B - Preparing Olympiad](https://codeforces.com/problemset/problem/550/B) | CF 1400 | Перебор подмножеств с несколькими ограничениями |

<a id="practice-sorting-compression"></a>

## 3. Сортировка, компараторы и сжатие координат

Этап **A0**. Core: **7**. Extra: **5**. Теория и признаки распознавания: [ROADMAP: сортировка](ROADMAP.md#topic-sorting-compression).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 912 - Sort an Array](https://leetcode.com/problems/sort-an-array/) | LC Medium | Базовая реализация сортировки |
| 2 | `Core` | [LC 56 - Merge Intervals](https://leetcode.com/problems/merge-intervals/) | LC Medium | Сортировка и слияние интервалов |
| 3 | `Core` | [ACMP 41 - Сортировка подсчетом](https://acmp.ru/index.asp?main=task&id_task=41) | - | Counting sort на малом диапазоне значений |
| 4 | `Core` | [ACMP 119 - Сортировка времени](https://acmp.ru/index.asp?main=task&id_task=119) | - | Компаратор объектов по составному временному ключу |
| 5 | `Core` | [CF 166A - Rank List](https://codeforces.com/problemset/problem/166/A) | CF 1100 | Сортировка пар по двум ключам и обработка равенств |
| 6 | `Core` | [CF 670C - Cinema](https://codeforces.com/problemset/problem/670/C) | CF 1300 | Сжатие значений через частоты и выбор по нескольким критериям |
| 7 | `Core` | [CF 230A - Dragons](https://codeforces.com/problemset/problem/230/A) | CF 1000 | Сортировка объектов и последовательный инвариант достижимости |
| 8 | `Extra` | [CF 141A - Amusing Joke](https://codeforces.com/problemset/problem/141/A) | CF 800 | Сортировка или частоты символов для сравнения мультимножеств |
| 9 | `Extra` | [CF 1849B - Monsters](https://codeforces.com/problemset/problem/1849/B) | CF 1000 | Компаратор по вычисляемому ключу и исходному индексу |
| 10 | `Extra` | [CF 1399A - Remove Smallest](https://codeforces.com/problemset/problem/1399/A) | CF 800 | Сортировка и локальная проверка соседних элементов |
| 11 | `Extra` | [CF 1201C - Maximum Median](https://codeforces.com/problemset/problem/1201/C) | CF 1400 | Сортировка и выравнивание суффикса вокруг медианы |
| 12 | `Extra` | [CF 978F - Mentors](https://codeforces.com/problemset/problem/978/F) | CF 1500 | Сортировка/сжатие с дублями и возвратом к исходным индексам |

<a id="practice-maps-sets"></a>

## 4. Частоты, HashMap/HashSet и множества

Этап **A0**. Core: **6**. Extra: **5**. Теория и признаки распознавания: [ROADMAP: частоты и множества](ROADMAP.md#topic-maps-sets).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 1 - Two Sum](https://leetcode.com/problems/two-sum/) | LC Easy | HashMap: поиск дополнения |
| 2 | `Core` | [LC 49 - Group Anagrams](https://leetcode.com/problems/group-anagrams/) | LC Medium | HashMap по каноническому ключу |
| 3 | `Core` | [ACMP 82 - Пересечение множеств](https://acmp.ru/index.asp?main=task&id_task=82) | - | Множество принадлежности и удаление дубликатов |
| 4 | `Core` | [CF 4C - Registration System](https://codeforces.com/problemset/problem/4/C) | CF 1300 | HashMap: чтение, проверка и обновление счётчика |
| 5 | `Core` | [CF 1520D - Same Differences](https://codeforces.com/problemset/problem/1520/D) | CF 1200 | Подсчёт пар по преобразованному ключу |
| 6 | `Core` | [CF 1791F - Range Update Point Query](https://codeforces.com/problemset/problem/1791/F) | CF 1500 | TreeSet.ceiling и удаление стабилизировавшихся индексов |
| 7 | `Extra` | [CF 1703B - ICPC Balloons](https://codeforces.com/problemset/problem/1703/B) | CF 800 | HashSet для первого появления элемента |
| 8 | `Extra` | [CF 1722C - Word Game](https://codeforces.com/problemset/problem/1722/C) | CF 800 | HashMap частот строк между несколькими наборами |
| 9 | `Extra` | [CF 1955B - Progressive Square](https://codeforces.com/problemset/problem/1955/B) | CF 1000 | Сравнение мультимножеств через частоты |
| 10 | `Extra` | [ACMP 816 - Система пересекающихся множеств](https://acmp.ru/index.asp?main=task&id_task=816) | - | Двусторонние списки принадлежности множествам |
| 11 | `Extra` | [CF 1108B - Divisors of Two Integers](https://codeforces.com/problemset/problem/1108/B) | CF 1100 | Мультимножество делителей и восстановление двух объектов |

<a id="practice-stack-queue-deque"></a>

## 5. Стек, очередь и дек

Этап **A0**. Core: **7**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: стек, очередь и дек](ROADMAP.md#topic-stack-queue-deque).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 20 - Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | LC Easy | стек для корректной вложенности |
| 2 | `Core` | [ACMP 899 - Баланс скобок](https://acmp.ru/index.asp?main=task&id_task=899) | - | Стек незакрытых скобок нескольких типов |
| 3 | `Core` | [CF 1234B2 - Social Network](https://codeforces.com/problemset/problem/1234/B2) | CF 1300 | Ограниченная FIFO-очередь плюс `HashSet` присутствующих элементов |
| 4 | `Core` | [CF 1579E1 - Permutation Minimization by Deque](https://codeforces.com/problemset/problem/1579/E1) | CF 1000 | Последовательный выбор `addFirst` или `addLast` |
| 5 | `Core` | [CF 1907B - YetnotherrokenKeoard](https://codeforces.com/problemset/problem/1907/B) | CF 1000 | Два независимых стека индексов и восстановление исходного порядка |
| 6 | `Core` | [CF 1428C - ABBB](https://codeforces.com/problemset/problem/1428/C) | CF 1100 | Потоковая редукция: новый символ взаимодействует только с вершиной стека |
| 7 | `Core` | Локальный checkpoint: расписание станков | Checkpoint | Дек для обычных и срочных задач; lazy deletion отмененных элементов при достижении головы |
| 8 | `Extra` | [CF 797C - Minimal string](https://codeforces.com/problemset/problem/797/C) | CF 1700 | Стек-буфер плюс минимум необработанного суффикса |

<a id="practice-priority-queue"></a>

## 6. Priority queue и heap

Этап **A0**. Core: **5**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: priority queue](ROADMAP.md#topic-priority-queue).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 703 - Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | LC Easy | heap из лучших `k` элементов |
| 2 | `Core` | [CF 1800C2 - Powering the Hero](https://codeforces.com/problemset/problem/1800/C2) | CF 1100 | Добавление бонусов в max-heap и извлечение лучшего по событию |
| 3 | `Core` | [CF Gym 102961T - Room Allocation](https://codeforces.com/gym/102961/problem/T) | - | Переиспользование ресурса с минимальным временем освобождения |
| 4 | `Core` | [CF 1353D - Constructing the Array](https://codeforces.com/problemset/problem/1353/D) | CF 1600 | Составной comparator: длина по убыванию, левая граница по возрастанию |
| 5 | `Core` | [CF 1468C - Berpizza](https://codeforces.com/problemset/problem/1468/C) | CF 1700 | Max-heap плюс FIFO/pointer, `served[]` и пропуск stale entries |
| 6 | `Extra` | [CF 1526C2 - Potions](https://codeforces.com/problemset/problem/1526/C2) | CF 1600 | Tentative selection и удаление худшего выбранного элемента |

<a id="practice-prefix-difference-2d"></a>

## 7. Префиксные суммы, массив разностей и 2D-префиксы

Этап **A1**. Core: **6**. Extra: **3**. Теория и признаки распознавания: [ROADMAP: префиксы и разности](ROADMAP.md#topic-prefix-difference-2d).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 303 - Range Sum Query Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | LC Easy | 1D-prefix |
| 2 | `Core` | [LC 304 - Range Sum Query 2D Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) | LC Medium | 2D-prefix |
| 3 | `Core` | [CF 816B - Karen and Coffee](https://codeforces.com/problemset/problem/816/B) | CF 1400 | Difference array для покрытия плюс второй prefix по предикату |
| 4 | `Core` | [CF 1722E - Counting Rectangles](https://codeforces.com/problemset/problem/1722/E) | CF 1600 | Взвешенный 2D-prefix и строгие границы прямоугольного запроса |
| 5 | `Core` | [CF 295A - Greg and Array](https://codeforces.com/problemset/problem/295/A) | CF 1400 | Два уровня offline difference arrays |
| 6 | `Core` | [CF 466C - Number of Ways](https://codeforces.com/problemset/problem/466/C) | CF 1700 | Подсчет упорядоченных пар точек разбиения по значениям префикса |
| 7 | `Extra` | [CF 1807D - Odd Queries](https://codeforces.com/problemset/problem/1807/D) | CF 900 | Префиксная сумма и виртуальная замена одного диапазона |
| 8 | `Extra` | [CF 1795C - Tea Tasting](https://codeforces.com/problemset/problem/1795/C) | CF 1500 | Binary search конца вклада, полные вклады через differences и один частичный край |
| 9 | `Extra` | [CF 276C - Little Girl and Maximum Sum](https://codeforces.com/problemset/problem/276/C) | CF 1500 | Частоты покрытия через differences плюс перестановочный greedy |

<a id="practice-two-pointers"></a>

## 8. Два указателя

Этап **A1**. Core: **4**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: два указателя](ROADMAP.md#topic-two-pointers).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 11 - Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | LC Medium | встречные указатели и доказанное отбрасывание кандидатов |
| 2 | `Core` | [CF Gym 102961G - Sum of Two Values](https://codeforces.com/gym/102961/problem/G) | - | Сортировка пар `(value, index)` и встречные указатели с восстановлением индексов |
| 3 | `Core` | [CF 489B - BerSU Ball](https://codeforces.com/problemset/problem/489/B) | CF 1200 | Greedy matching двух отсортированных групп |
| 4 | `Core` | [CF 1036D - Vasya and Arrays](https://codeforces.com/problemset/problem/1036/D) | CF 1600 | Синхронный проход по двум массивам и закрытие блоков при равенстве сумм |
| 5 | `Extra` | [CF 1669F - Eating Candies](https://codeforces.com/problemset/problem/1669/F) | CF 1100 | Синхронизация положительных накопленных сумм с двух концов |
| 6 | `Extra` | [CF 1538C - Number of Pairs](https://codeforces.com/problemset/problem/1538/C) | CF 1300 | Решить через линейный `count(sum <= x)` двумя указателями, не отдельными binary searches |

<a id="practice-sliding-window"></a>

## 9. Sliding window и monotonic deque

Этап **A1**. Core: **7**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: sliding window](ROADMAP.md#topic-sliding-window).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 3 - Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | LC Medium | частотное окно |
| 2 | `Core` | [LC 239 - Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | LC Hard | monotonic deque |
| 3 | `Core` | [CF 1690D - Black and White Stripe](https://codeforces.com/problemset/problem/1690/D) | CF 1000 | Фиксированное rolling window: добавить справа и удалить вышедший символ |
| 4 | `Core` | [CF 279B - Books](https://codeforces.com/problemset/problem/279/B) | CF 1400 | Максимальное variable window с ограничением на сумму положительных элементов |
| 5 | `Core` | [CF 701C - They Are Everywhere](https://codeforces.com/problemset/problem/701/C) | CF 1500 | Minimum-cover window с общей таблицей частот |
| 6 | `Core` | [CF Gym 102961ZD - Subarray Distinct Values](https://codeforces.com/gym/102961/problem/ZD) | - | Подсчет подмассивов с `at most k` различными через `answer += r - l + 1` |
| 7 | `Core` | [CF 6E - Exposition](https://codeforces.com/problemset/problem/6/E) | CF 1900 | Самое длинное окно с `max-min <= k` строго через два monotonic deque, без `TreeSet` и segment tree |
| 8 | `Extra` | [CF 580B - Kefa and Company](https://codeforces.com/problemset/problem/580/B) | CF 1500 | Сортировка по ключу плюс variable window и `long`-сумма |
| 9 | `Extra` | [CF 1358D - The Best Vacation](https://codeforces.com/problemset/problem/1358/D) | CF 1900 | Циклическое взвешенное окно и частично взятый край |

<a id="practice-monotonic-stack"></a>

## 10. Монотонный стек

Этап **A1**. Core: **5**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: монотонный стек](ROADMAP.md#topic-monotonic-stack).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 739 - Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | LC Medium | next greater |
| 2 | `Core` | [LC 84 - Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | LC Hard | границы области высоты |
| 3 | `Core` | [CF Gym 102961Z - Nearest Smaller Values](https://codeforces.com/gym/102961/problem/Z) | - | Previous strictly smaller; при равенстве требуется `pop >=` |
| 4 | `Core` | [CF 547B - Mike and Feet](https://codeforces.com/problemset/problem/547/B) | CF 1900 | Ближайшие меньшие с двух сторон, span и распространение ответа по длинам |
| 5 | `Core` | [CF 817D - Imbalanced Array](https://codeforces.com/problemset/problem/817/D) | CF 1900 | Contribution counting для `sum(max-min)` с асимметричными tie rules |
| 6 | `Extra` | [CF 1886C - Decreasing String](https://codeforces.com/problemset/problem/1886/C) | CF 1600 | Greedy deletion через удаление больших символов с вершины |
| 7 | `Extra` | [CF 1313C2 - Skyscrapers](https://codeforces.com/problemset/problem/1313/C2) | CF 1900 | Stack DP для clipped prefix/suffix и восстановление оптимального массива |

<a id="practice-sweep-line"></a>

## 11. Sweep line

Этап **A1**. Core: **4**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: sweep line](ROADMAP.md#topic-sweep-line).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 1000C - Covered Points Count](https://codeforces.com/problemset/problem/1000/C) | CF 1700 | Difference events на закрытых целочисленных интервалах и длины по числу покрытий |
| 2 | `Core` | [CF 612D - The Union of k-Segments](https://codeforces.com/problemset/problem/612/D) | CF 1800 | Равные координаты, порог покрытия и восстановление итоговых отрезков |
| 3 | `Core` | [CF 1249D2 - Too Many Segments](https://codeforces.com/problemset/problem/1249/D2) | CF 1800 | Active set и greedy-удаление интервала с максимальной правой границей |
| 4 | `Core` | [CF 1420D - Rescue Nibel](https://codeforces.com/problemset/problem/1420/D) | CF 1800 | Считать каждую группу в момент открытия последнего интервала; открытия раньше закрытий |
| 5 | `Extra` | [CF 1284D - New Year and Conference](https://codeforces.com/problemset/problem/1284/D) | CF 2100 | Два симметричных sweep line и active multiset для проверки пересечений |

<a id="practice-binary-search"></a>

## 12. Бинарный/тернарный поиск и поиск по ответу

Этап **A1**. Core: **5**. Extra: **7**. Теория и признаки распознавания: [ROADMAP: binary search](ROADMAP.md#topic-binary-search).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 704 - Binary Search](https://leetcode.com/problems/binary-search/) | LC Easy | Классический binary search |
| 2 | `Core` | [LC 875 - Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | LC Medium | Binary search on answer |
| 3 | `Core` | [ACMP 267 - Ксерокопии](https://acmp.ru/index.asp?main=task&id_task=267) | - | First true: минимальное время производства |
| 4 | `Core` | [CF 706B - Interesting drink](https://codeforces.com/problemset/problem/706/B) | CF 1100 | Upper bound: число элементов не больше x |
| 5 | `Core` | [CF 1742E - Scuza](https://codeforces.com/problemset/problem/1742/E) | CF 1200 | Upper bound по максимумам префикса + сумма префикса |
| 6 | `Extra` | [CF 474B - Worms](https://codeforces.com/problemset/problem/474/B) | CF 1200 | Lower bound по монотонным префиксным границам |
| 7 | `Extra` | [CF 1352C - K-th Not Divisible by n](https://codeforces.com/problemset/problem/1352/C) | CF 1200 | Поиск k-го допустимого числа по монотонному счётчику |
| 8 | `Extra` | [CF 670D1 - Magic Powder - 1](https://codeforces.com/problemset/problem/670/D1) | CF 1400 | Binary search on answer + линейная can(x) |
| 9 | `Extra` | [CF 1873E - Building an Aquarium](https://codeforces.com/problemset/problem/1873/E) | CF 1100 | Поиск максимальной высоты при ограниченной стоимости |
| 10 | `Extra` | [ACMP 523 - Роман в томах](https://acmp.ru/index.asp?main=task&id_task=523) | - | Минимизация максимального блока через greedy can(x) |
| 11 | `Extra` | [CF 371C - Hamburgers](https://codeforces.com/problemset/problem/371/C) | CF 1600 | Поиск ответа с аккуратной верхней границей и long |
| 12 | `Extra` | [CF 1355E - Restorer Distance](https://codeforces.com/problemset/problem/1355/E) | CF 2100 | Дискретная унимодальность и тернарный поиск стоимости |

<a id="practice-greedy"></a>

## 13. Жадные алгоритмы, инварианты и обменный аргумент

Этап **A1**. Core: **5**. Extra: **8**. Теория и признаки распознавания: [ROADMAP: greedy](ROADMAP.md#topic-greedy).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 55 - Jump Game](https://leetcode.com/problems/jump-game/) | LC Medium | Greedy-инвариант дальней достижимой позиции |
| 2 | `Core` | [LC 435 - Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | LC Medium | Interval scheduling по правому концу |
| 3 | `Core` | [CF 514A - Chewbaсca and Number](https://codeforces.com/problemset/problem/514/A) | CF 1200 | Независимый локально оптимальный выбор |
| 4 | `Core` | [CF 158B - Taxi](https://codeforces.com/problemset/problem/158/B) | CF 1100 | Жадная упаковка групп ограниченных размеров |
| 5 | `Core` | [CF 545C - Woodcutters](https://codeforces.com/problemset/problem/545/C) | CF 1500 | Жадная обработка интервалов слева направо |
| 6 | `Extra` | [CF 34B - Sale](https://codeforces.com/problemset/problem/34/B) | CF 900 | Выбор фиксированного числа наиболее выгодных элементов |
| 7 | `Extra` | [CF 337A - Puzzles](https://codeforces.com/problemset/problem/337/A) | CF 900 | Минимальный диапазон после сортировки |
| 8 | `Extra` | [CF 545D - Queue](https://codeforces.com/problemset/problem/545/D) | CF 1300 | Scheduling: сортировка и инвариант принятого префикса |
| 9 | `Extra` | [CF 58A - Chat room](https://codeforces.com/problemset/problem/58/A) | CF 1000 | Жадное распознавание подпоследовательности |
| 10 | `Extra` | [CF 1041C - Coffee Break](https://codeforces.com/problemset/problem/1041/C) | CF 1600 | Жадное распределение событий через ordered set |
| 11 | `Extra` | [CF 853A - Planning](https://codeforces.com/problemset/problem/853/A) | CF 1500 | Priority queue и выбор максимальной текущей потери |
| 12 | `Extra` | [ACMP 39 - Волосатый бизнес](https://acmp.ru/index.asp?main=task&id_task=39) | - | Суффиксный максимум и доказательство момента действия |
| 13 | `Extra` | [CF 1365D - Solve The Maze](https://codeforces.com/problemset/problem/1365/D) | CF 1700 | Локальное жадное блокирование + проверка достижимости |

<a id="practice-bitmasks"></a>

## 14. Биты, маски, подмаски и булева алгебра

Этап **A1**. Core: **5**. Extra: **7**. Теория и признаки распознавания: [ROADMAP: биты и маски](ROADMAP.md#topic-bitmasks).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 1239 - Maximum Length of a Concatenated String with Unique Characters](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/) | LC Medium | Битовая маска множества и проверка конфликтов |
| 2 | `Core` | [LC 1310 - XOR Queries of a Subarray](https://leetcode.com/problems/xor-queries-of-a-subarray/) | LC Medium | Префиксный XOR |
| 3 | `Core` | [ACMP 542 - Бит-реверс](https://acmp.ru/index.asp?main=task&id_task=542) | - | Извлечение битов и построение числа сдвигами |
| 4 | `Core` | [CF 1420B - Rock and Lever](https://codeforces.com/problemset/problem/1420/B) | CF 1200 | Группировка по старшему установленному биту |
| 5 | `Core` | [CF 1516B - AGAGA XOOORRR](https://codeforces.com/problemset/problem/1516/B) | CF 1500 | Префиксный XOR и разбиение на равные XOR-сегменты |
| 6 | `Extra` | [CF 579A - Raising Bacteria](https://codeforces.com/problemset/problem/579/A) | CF 1000 | Popcount как минимальное число степеней двойки |
| 7 | `Extra` | [CF 1559A - Mocha and Math](https://codeforces.com/problemset/problem/1559/A) | CF 900 | Сведение последовательности побитовым AND |
| 8 | `Extra` | [CF 467B - Fedor and New Game](https://codeforces.com/problemset/problem/467/B) | CF 1100 | XOR двух масок и popcount различий |
| 9 | `Extra` | [CF 1362C - Johnny and Another Rating Drop](https://codeforces.com/problemset/problem/1362/C) | CF 1400 | Вклады младших битов при последовательном изменении числа |
| 10 | `Extra` | [CF 1095C - Powers Of Two](https://codeforces.com/problemset/problem/1095/C) | CF 1400 | Разбиение числа на степени двойки через heap/lowbit |
| 11 | `Extra` | [CF 1552D - Array Differentiation](https://codeforces.com/problemset/problem/1552/D) | CF 1800 | Явный перебор подмасок циклом sub=(sub-1)&mask |
| 12 | `Extra` | [CF 449D - Jzzhu and Numbers](https://codeforces.com/problemset/problem/449/D) | CF 2400 | SOS DP по маскам + inclusion-exclusion |

<a id="practice-number-theory"></a>

## 15. Теория чисел: gcd, простые, факторизация, решето

Этап **A1**. Core: **6**. Extra: **9**. Теория и признаки распознавания: [ROADMAP: теория чисел](ROADMAP.md#topic-number-theory).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 204 - Count Primes](https://leetcode.com/problems/count-primes/) | LC Medium | Решето Эратосфена |
| 2 | `Core` | [LC 1979 - Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) | LC Easy | Алгоритм Евклида |
| 3 | `Core` | [CF 546D - Soldier and Number Game](https://codeforces.com/problemset/problem/546/D) | CF 1700 | SPF-sieve и префикс числа простых множителей с кратностью |
| 4 | `Core` | [CF 1294C - Product of Three Numbers](https://codeforces.com/problemset/problem/1294/C) | CF 1300 | Пробное деление и выделение множителей за O(sqrt n) |
| 5 | `Core` | [CF 7C - Line](https://codeforces.com/problemset/problem/7/C) | CF 1800 | Extended gcd и линейное диофантово уравнение |
| 6 | `Core` | [CF 687B - Remainders Game](https://codeforces.com/problemset/problem/687/B) | CF 1800 | CRT-интуиция: достаточность набора модулей через LCM |
| 7 | `Extra` | [ACMP 14 - НОК](https://acmp.ru/index.asp?main=task&id_task=14) | - | GCD/LCM и безопасный порядок умножения |
| 8 | `Extra` | [CF 17A - Noldbach problem](https://codeforces.com/problemset/problem/17/A) | CF 1000 | Решето простых и проверка специального представления |
| 9 | `Extra` | [CF 230B - T-primes](https://codeforces.com/problemset/problem/230/B) | CF 1300 | Решето + проверка квадрата простого числа |
| 10 | `Extra` | [CF 26A - Almost Prime](https://codeforces.com/problemset/problem/26/A) | CF 900 | Подсчёт различных простых делителей для всех чисел |
| 11 | `Extra` | [CF 762A - k-th divisor](https://codeforces.com/problemset/problem/762/A) | CF 1400 | Перечисление делителей за O(sqrt n) в возрастающем порядке |
| 12 | `Extra` | [CF 1295D - Same GCDs](https://codeforces.com/problemset/problem/1295/D) | CF 1800 | Преобразование gcd-условия к функции Эйлера |
| 13 | `Extra` | [CF 1627D - Not Adding](https://codeforces.com/problemset/problem/1627/D) | CF 1900 | Sieve-like обработка gcd по всем кратным |
| 14 | `Extra` | [CF 1500B - Two chandeliers](https://codeforces.com/problemset/problem/1500/B) | CF 2200 | Generalized CRT + gcd-совместимость + поиск по ответу |
| 15 | `Extra` | [CF 710D - Two Arithmetic Progressions](https://codeforces.com/problemset/problem/710/D) | CF 2500 | Линейные сравнения и CRT для пересечения прогрессий |

<a id="practice-modular-combinatorics"></a>

## 16. Модульная арифметика и комбинаторика

Этап **A1**. Core: **6**. Extra: **7**. Теория и признаки распознавания: [ROADMAP: модульная арифметика](ROADMAP.md#topic-modular-combinatorics).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 62 - Unique Paths](https://leetcode.com/problems/unique-paths/) | LC Medium | Подсчёт путей: DP или сочетания |
| 2 | `Core` | [LC 1641 - Count Sorted Vowel Strings](https://leetcode.com/problems/count-sorted-vowel-strings/) | LC Medium | Комбинации с повторениями |
| 3 | `Core` | [CF 1514B - AND 0, Sum Big](https://codeforces.com/problemset/problem/1514/B) | CF 1200 | Быстрое возведение в степень по модулю |
| 4 | `Core` | [CF 1444B - Divide and Sum](https://codeforces.com/problemset/problem/1444/B) | CF 1900 | Factorial/invfactorial и центральный биномиальный коэффициент |
| 5 | `Core` | [CF 340E - Iahub and Permutations](https://codeforces.com/problemset/problem/340/E) | CF 2000 | Derangements и inclusion-exclusion |
| 6 | `Core` | [CF 1305C - Kuroni and Impossible Calculation](https://codeforces.com/problemset/problem/1305/C) | CF 1600 | Принцип Дирихле + произведение попарных разностей |
| 7 | `Extra` | [ACMP 158 - Великий комбинатор](https://acmp.ru/index.asp?main=task&id_task=158) | - | Комбинаторная модель распределения с повторениями |
| 8 | `Extra` | [CF 553A - Kyoya and Colored Balls](https://codeforces.com/problemset/problem/553/A) | CF 1500 | Последовательное применение сочетаний |
| 9 | `Extra` | [CF 459B - Pashmak and Flowers](https://codeforces.com/problemset/problem/459/B) | CF 1300 | Подсчёт пар экстремальных значений |
| 10 | `Extra` | [CF 478B - Random Teams](https://codeforces.com/problemset/problem/478/B) | CF 1300 | Экстремальное распределение и C(x,2) |
| 11 | `Extra` | [CF 1436C - Binary Search](https://codeforces.com/problemset/problem/1436/C) | CF 1500 | Комбинаторное моделирование пути binary search |
| 12 | `Extra` | [CF 300C - Beautiful Numbers](https://codeforces.com/problemset/problem/300/C) | CF 1800 | Factorial/invfactorial + перебор числа выбранных цифр |
| 13 | `Extra` | [CF 451E - Devu and Flowers](https://codeforces.com/problemset/problem/451/E) | CF 2300 | Inclusion-exclusion по верхним ограничениям + сочетания |

<a id="practice-basic-strings"></a>

## 17. Строки: префикс-функция, Z-функция и хеширование

Этап **A1**. Core: **6**. Extra: **6**. Теория и признаки распознавания: [ROADMAP: базовые строки](ROADMAP.md#topic-basic-strings).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 28 - Find the Index of the First Occurrence](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | LC Easy | Базовый поиск подстроки |
| 2 | `Core` | [LC 214 - Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) | LC Hard | KMP и палиндромный префикс |
| 3 | `Core` | Локальный checkpoint: базовые строковые функции | Checkpoint | Реализовать prefix function, Z-function и двойной polynomial hash; одним поиском проверить KMP и Z-function |
| 4 | `Core` | [ACMP 202 - Поиск подстроки](https://acmp.ru/index.asp?main=task&id_task=202) | - | KMP/Z: поиск всех вхождений образца |
| 5 | `Core` | [ACMP 204 - Циклическая строка](https://acmp.ru/index.asp?main=task&id_task=204) | - | Граница строки и минимальный период |
| 6 | `Core` | [CF 432D - Prefixes and Suffixes](https://codeforces.com/problemset/problem/432/D) | CF 2000 | Z-function и подсчёт вхождений всех границ |
| 7 | `Extra` | [CF 126B - Password](https://codeforces.com/problemset/problem/126/B) | CF 1700 | Дерево границ prefix=suffix и внутреннее вхождение |
| 8 | `Extra` | [CF 471D - MUH and Cube Walls](https://codeforces.com/problemset/problem/471/D) | CF 1800 | KMP/Z по массиву разностей |
| 9 | `Extra` | [CF 1200E - Compress Words](https://codeforces.com/problemset/problem/1200/E) | CF 2000 | Максимальное prefix/suffix перекрытие при последовательном слиянии |
| 10 | `Extra` | [CF 535D - Tavas and Malekas](https://codeforces.com/problemset/problem/535/D) | CF 1900 | Z-function для проверки совместимости перекрывающихся шаблонов |
| 11 | `Extra` | [CF 7D - Palindrome Degree](https://codeforces.com/problemset/problem/7/D) | CF 2200 | Rolling hash + DP по палиндромным префиксам |
| 12 | `Extra` | [CF 271D - Good Substrings](https://codeforces.com/problemset/problem/271/D) | CF 1800 | Trie или rolling hash для различных подстрок с ограничением |

<a id="practice-graph-traversals"></a>

## 18. Обходы графа, компоненты, циклы и двудольность

Этап **A1**. Core: **5**. Extra: **5**. Теория и признаки распознавания: [ROADMAP: обходы графа](ROADMAP.md#topic-graph-traversals).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 200 - Number of Islands](https://leetcode.com/problems/number-of-islands/) | LC Medium | Flood fill компонент |
| 2 | `Core` | [LC 785 - Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) | LC Medium | Двудольная раскраска |
| 3 | `Core` | [ACMP 99 - Лабиринт](https://acmp.ru/index.asp?main=task&id_task=99) | - | BFS в трёхмерном лабиринте |
| 4 | `Core` | [CF 510B - Fox And Two Dots](https://codeforces.com/problemset/problem/510/B) | CF 1500 | Цикл в неориентированной сетке с parent |
| 5 | `Core` | [CF 1829E - The Lakes](https://codeforces.com/problemset/problem/1829/E) | CF 1100 | Flood fill компонент с агрегированием веса |
| 6 | `Extra` | [CF 217A - Ice Skating](https://codeforces.com/problemset/problem/217/A) | CF 1200 | Компоненты в неявно заданном графе |
| 7 | `Extra` | [CF 500A - New Year Transportation](https://codeforces.com/problemset/problem/500/A) | CF 1000 | Достижимость в функциональном ориентированном графе |
| 8 | `Extra` | [CF 687A - NP-Hard Problem](https://codeforces.com/problemset/problem/687/A) | CF 1500 | Двудольная раскраска общего графа |
| 9 | `Extra` | [CF 1702E - Split Into Two Sets](https://codeforces.com/problemset/problem/1702/E) | CF 1600 | Степени + двудольность графа из пар |
| 10 | `Extra` | [CF 377A - Maze](https://codeforces.com/problemset/problem/377/A) | CF 1600 | DFS по сетке с сохранением связной части |

<a id="practice-shortest-paths"></a>

## 19. Кратчайшие пути: BFS, 0-1 BFS, Дейкстра, Флойд, Беллман-Форд

Этап **A1**. Core: **6**. Extra: **6**. Теория и признаки распознавания: [ROADMAP: кратчайшие пути](ROADMAP.md#topic-shortest-paths).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 743 - Network Delay Time](https://leetcode.com/problems/network-delay-time/) | LC Medium | Dijkstra по списку рёбер |
| 2 | `Core` | [LC 787 - Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | LC Medium | DP/Bellman-Ford с ограничением числа рёбер |
| 3 | `Core` | [CF 520B - Two Buttons](https://codeforces.com/problemset/problem/520/B) | CF 1400 | BFS по неявному графу состояний |
| 4 | `Core` | [CF 1063B - Labyrinth](https://codeforces.com/problemset/problem/1063/B) | CF 1800 | 0-1 BFS: стоимость горизонтального перехода |
| 5 | `Core` | [ACMP 135 - Алгоритм Флойда](https://acmp.ru/index.asp?main=task&id_task=135) | - | Floyd-Warshall: все пары кратчайших путей |
| 6 | `Core` | [CF 20C - Dijkstra?](https://codeforces.com/problemset/problem/20/C) | CF 1900 | Dijkstra + parent[] + восстановление пути |
| 7 | `Extra` | [ACMP 132 - Алгоритм Дейкстры](https://acmp.ru/index.asp?main=task&id_task=132) | - | Dijkstra: релаксация и выбор минимального расстояния |
| 8 | `Extra` | [ACMP 138 - Алгоритм Форда-Беллмана](https://acmp.ru/index.asp?main=task&id_task=138) | - | Bellman-Ford на графе с отрицательными рёбрами |
| 9 | `Extra` | [CF 938D - Buy a Ticket](https://codeforces.com/problemset/problem/938/D) | CF 2000 | Multi-source Dijkstra с разными начальными расстояниями |
| 10 | `Extra` | [CF 295B - Greg and Graph](https://codeforces.com/problemset/problem/295/B) | CF 1700 | Обратное добавление вершин во Floyd |
| 11 | `Extra` | [ACMP 140 - Цикл отрицательного веса](https://acmp.ru/index.asp?main=task&id_task=140) | - | Обнаружение и восстановление отрицательного цикла |
| 12 | `Extra` | [CF 449B - Jzzhu and Cities](https://codeforces.com/problemset/problem/449/B) | CF 2000 | Dijkstra с несколькими типами стартовых рёбер |

<a id="practice-trees-lca"></a>

## 20. Деревья: Эйлеров обход, двоичные подъёмы и LCA

Этап **A1**. Core: **6**. Extra: **9**. Теория и признаки распознавания: [ROADMAP: деревья и LCA](ROADMAP.md#topic-trees-lca).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 236 - Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | LC Medium | Lowest common ancestor |
| 2 | `Core` | [LC 863 - All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | LC Medium | Расстояния в дереве |
| 3 | `Core` | [CF 1006E - Military Problem](https://codeforces.com/problemset/problem/1006/E) | CF 1600 | Euler/preorder flatten + размер поддерева |
| 4 | `Core` | Локальный checkpoint: базовые алгоритмы на деревьях | Checkpoint | Parent/depth/subtree size, диаметр с восстановлением и binary lifting для k-го предка |
| 5 | `Core` | [CF 191C - Fools and Roads](https://codeforces.com/problemset/problem/191/C) | CF 1900 | LCA + разности на дереве + postorder-накопление |
| 6 | `Core` | [CF 1328E - Tree Queries](https://codeforces.com/problemset/problem/1328/E) | CF 1900 | Ancestor relation через tin/tout |
| 7 | `Extra` | [ACMP 141 - Дерево](https://acmp.ru/index.asp?main=task&id_task=141) | - | Проверка структуры дерева |
| 8 | `Extra` | [CF 115A - Party](https://codeforces.com/problemset/problem/115/A) | CF 900 | Родители, глубины и высота леса |
| 9 | `Extra` | [CF 1057A - Bmail Computer Network](https://codeforces.com/problemset/problem/1057/A) | CF 900 | Восстановление пути от вершины к корню по parent[] |
| 10 | `Extra` | [CF 580C - Kefa and Park](https://codeforces.com/problemset/problem/580/C) | CF 1500 | Корневой DFS с состоянием на пути |
| 11 | `Extra` | [CF 1676G - White-Black Balanced Subtrees](https://codeforces.com/problemset/problem/1676/G) | CF 1300 | Агрегирование баланса по поддереву |
| 12 | `Extra` | [CF 1304E - 1-Trees and Queries](https://codeforces.com/problemset/problem/1304/E) | CF 2000 | LCA, расстояния и чётность маршрута с дополнительным ребром |
| 13 | `Extra` | [CF Gym 100091B - LCA Продолжение](https://codeforces.com/gym/100091/problem/B) ; [регистрация/отправка](https://codeforces.com/gym/100091) | - | Online LCA: двоичные подъёмы при добавлении листьев |
| 14 | `Extra` | [CF 519E - A and B and Lecture Rooms](https://codeforces.com/problemset/problem/519/E) | CF 2100 | Binary lifting + размеры частей дерева |
| 15 | `Extra` | [CF 383C - Propagating tree](https://codeforces.com/problemset/problem/383/C) | CF 2000 | Euler flatten + Fenwick с учётом чётности глубины |

<a id="practice-basic-dp"></a>

## 21. Базовое DP: пути, рюкзак, LIS и восстановление ответа

Этап **A1**. Core: **7**. Extra: **9**. Теория и признаки распознавания: [ROADMAP: базовое DP](ROADMAP.md#topic-basic-dp).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 322 - Coin Change](https://leetcode.com/problems/coin-change/) | LC Medium | Unbounded knapsack |
| 2 | `Core` | [LC 300 - Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | LC Medium | Longest increasing subsequence |
| 3 | `Core` | Локальный checkpoint: классическое DP | Checkpoint | Grid paths, coin change, 0/1 knapsack, LCS, edit distance и LIS с восстановлением |
| 4 | `Core` | [ACMP 11 - Зайчик](https://acmp.ru/index.asp?main=task&id_task=11) | - | Число способов и одномерная рекуррентность |
| 5 | `Core` | [CF 698A - Vacations](https://codeforces.com/problemset/problem/698/A) | CF 1400 | Малое состояние предыдущего действия |
| 6 | `Core` | [CF 455A - Boredom](https://codeforces.com/problemset/problem/455/A) | CF 1500 | Сжатие частот + choose/skip DP |
| 7 | `Core` | [CF 706C - Hard problem](https://codeforces.com/problemset/problem/706/C) | CF 1600 | Два состояния строки, INF и переходы |
| 8 | `Extra` | [ACMP 121 - Гвоздики](https://acmp.ru/index.asp?main=task&id_task=121) | - | Одномерное DP после сортировки |
| 9 | `Extra` | [CF 189A - Cut Ribbon](https://codeforces.com/problemset/problem/189/A) | CF 1300 | Unbounded knapsack на максимум числа предметов |
| 10 | `Extra` | [CF 474D - Flowers](https://codeforces.com/problemset/problem/474/D) | CF 1700 | Число способов набрать сумму переходами двух размеров |
| 11 | `Extra` | [CF 327A - Flipping Game](https://codeforces.com/problemset/problem/327/A) | CF 1200 | DP максимального подотрезка после преобразования выигрыша |
| 12 | `Extra` | [CF 1195C - Basketball Exercise](https://codeforces.com/problemset/problem/1195/C) | CF 1400 | Prefix DP с двумя рядами |
| 13 | `Extra` | [CF 4D - Mysterious Present](https://codeforces.com/problemset/problem/4/D) | CF 1700 | LIS-подобное DP + parent для восстановления |
| 14 | `Extra` | [CF 977F - Consecutive Subsequence](https://codeforces.com/problemset/problem/977/F) | CF 1700 | DP по значению с восстановлением индексов подпоследовательности |
| 15 | `Extra` | [CF 577B - Modulo Sum](https://codeforces.com/problemset/problem/577/B) | CF 1900 | 0/1 subset-sum DP по остаткам + pigeonhole |
| 16 | `Extra` | [CF 864E - Fire](https://codeforces.com/problemset/problem/864/E) | CF 2000 | 0/1 knapsack с дедлайнами и восстановлением набора |

<a id="practice-fenwick"></a>

## 22. Fenwick tree

Этап **A1**. Core: **4**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: Fenwick](ROADMAP.md#topic-fenwick).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 307 - Range Sum Query Mutable](https://leetcode.com/problems/range-sum-query-mutable/) | LC Medium | point update и range sum |
| 2 | `Core` | [ACMP 1084 - Дерево Фенвика](https://acmp.ru/index.asp?main=task&id_task=1084) | - | Базовый `add`, prefix sum и range sum |
| 3 | `Core` | [CF 652D - Nested Segments](https://codeforces.com/problemset/problem/652/D) | CF 1800 | Offline dominance: сортировка по одной границе и Fenwick по другой |
| 4 | `Core` | [CF 1208D - Restore Permutation](https://codeforces.com/problemset/problem/1208/D) | CF 1900 | Поиск позиции по взвешенной префиксной сумме спуском по Fenwick |
| 5 | `Extra` | [CF 459D - Pashmak and Parmida's problem](https://codeforces.com/problemset/problem/459/D) | CF 1800 | Преобразование элементов в частотные ранги и подсчет пар Fenwick-ом |
| 6 | `Extra` | [CF 61E - Enemy is weak](https://codeforces.com/problemset/problem/61/E) | CF 1900 | Вклад среднего элемента в убывающие тройки через два направления |

<a id="practice-segment-tree"></a>

## 23. Segment tree и lazy propagation

Этап **A1**. Core: **5**. Extra: **3**. Теория и признаки распознавания: [ROADMAP: segment tree](ROADMAP.md#topic-segment-tree).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [ACMP 1185 - RMQ с изменением элемента](https://acmp.ru/index.asp?main=task&id_task=1185) | - | Point assignment и range maximum |
| 2 | `Core` | [CF 339D - Xenia and Bit Operations](https://codeforces.com/problemset/problem/339/D) | CF 1700 | Point update и merge, зависящий от уровня дерева |
| 3 | `Core` | [CF 380C - Sereja and Brackets](https://codeforces.com/problemset/problem/380/C) | CF 2000 | Собственный ассоциативный узел для скобочной последовательности |
| 4 | `Core` | Локальный checkpoint: segment tree и lazy | Checkpoint | Range add + range min; stress-test против массива; композиция add и assign |
| 5 | `Core` | [CF 52C - Circular RMQ](https://codeforces.com/problemset/problem/52/C) | CF 2200 | `range add + range min`, lazy tags и разбиение циклического диапазона |
| 6 | `Extra` | [LC 715 - Range Module](https://leetcode.com/problems/range-module/) | LC Hard | динамическое покрытие диапазонов и lazy propagation |
| 7 | `Extra` | [CF 242E - XOR on Segment](https://codeforces.com/problemset/problem/242/E) | CF 2000 | Побитовый составной узел и lazy range xor |
| 8 | `Extra` | [CF 438D - The Child and Sequence](https://codeforces.com/problemset/problem/438/D) | CF 2300 | Амортизированное pruning по максимуму для modulo; это не стандартный lazy |

<a id="practice-static-rmq"></a>

## 24. Static RMQ и sparse table

Этап **A1**. Core: **4**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: static RMQ](ROADMAP.md#topic-static-rmq).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: sparse table | Checkpoint | Построить RMQ min и сверить все непустые диапазоны случайных массивов с наивным ответом |
| 2 | `Core` | [CF 1709D - Rorororobot](https://codeforces.com/problemset/problem/1709/D) | CF 1700 | Static range maximum плюс арифметическая достижимость |
| 3 | `Core` | [CF 1548B - Integers Have Friends](https://codeforces.com/problemset/problem/1548/B) | CF 1800 | GCD sparse table на соседних разностях и монотонный поиск границы |
| 4 | `Core` | [CF 359D - Pair of Numbers](https://codeforces.com/problemset/problem/359/D) | CF 2000 | Две static tables для `min` и `gcd`, binary search длины и восстановление всех ответов |
| 5 | `Extra` | [CF 474F - Ant Colony](https://codeforces.com/problemset/problem/474/F) | CF 2100 | GCD/min диапазона плюс частота точного значения через списки позиций |
| 6 | `Extra` | [CF 689D - Friends and Subsequences](https://codeforces.com/problemset/problem/689/D) | CF 2100 | Сравнить два решения: sparse table плюс binary searches и linear monotonic deques |

<a id="practice-geometry"></a>

## 25. Вычислительная геометрия

Этап **B**. Core: **6**. Extra: **3**. Теория и признаки распознавания: [ROADMAP: геометрия](ROADMAP.md#topic-geometry).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 149 - Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/) | LC Hard | Коллинеарность и нормализация направления |
| 2 | `Core` | [ACMP 348 - Пересечение отрезков](https://acmp.ru/index.asp?main=task&id_task=348) | - | Orientation + point-on-segment + пересечение отрезков |
| 3 | `Core` | [ACMP 370 - Площадь многоугольника](https://acmp.ru/index.asp?main=task&id_task=370) | - | Площадь многоугольника через shoelace/cross product |
| 4 | `Core` | [CF 772B - Volatile Kite](https://codeforces.com/problemset/problem/772/B) | CF 1800 | Расстояние от точки до прямой через cross product |
| 5 | `Core` | [ACMP 374 - Выпуклая оболочка - 2](https://acmp.ru/index.asp?main=task&id_task=374) | - | Выпуклая оболочка и обработка коллинеарных точек |
| 6 | `Core` | [CF Gym 101554D - Robert Hood](https://codeforces.com/gym/101554/problem/D) ; [регистрация/отправка](https://codeforces.com/gym/101554) | - | Convex hull + rotating calipers для диаметра множества |
| 7 | `Extra` | [LC 973 - K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | LC Medium | Расстояния и выбор k объектов |
| 8 | `Extra` | [CF 993A - Two Squares](https://codeforces.com/problemset/problem/993/A) | CF 1600 | Пересечения сторон + containment выпуклых фигур |
| 9 | `Extra` | [CF 166B - Polygons](https://codeforces.com/problemset/problem/166/B) | CF 2100 | Строгое попадание выпуклого многоугольника без касаний |

<a id="practice-advanced-graphs"></a>

## 26. DAG, топосортировка, SCC, мосты и точки сочленения

Этап **B**. Core: **6**. Extra: **5**. Теория и признаки распознавания: [ROADMAP: продвинутые графы](ROADMAP.md#topic-advanced-graphs).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 1192 - Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) | LC Hard | Мосты через tin/low |
| 2 | `Core` | [LC 802 - Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/) | LC Medium | Состояния вершин ориентированного графа |
| 3 | `Core` | [CF 510C - Fox And Names](https://codeforces.com/problemset/problem/510/C) | CF 1600 | Топологическая сортировка + невозможный префикс строк |
| 4 | `Core` | [CF 427C - Checkposts](https://codeforces.com/problemset/problem/427/C) | CF 1700 | SCC + агрегирование минимума и числа вариантов |
| 5 | `Core` | [CF Gym 100083D - Точки сочленения](https://codeforces.com/gym/100083/problem/D) ; [регистрация/отправка](https://codeforces.com/gym/100083) | - | Точки сочленения через tin/low |
| 6 | `Core` | [CF 1000E - We Need More Bosses](https://codeforces.com/problemset/problem/1000/E) | CF 2100 | Мосты + сжатие 2-edge-connected components + диаметр |
| 7 | `Extra` | [CF 919D - Substring](https://codeforces.com/problemset/problem/919/D) | CF 1700 | Topological order + DAG DP |
| 8 | `Extra` | [CF 1217D - Coloring Edges](https://codeforces.com/problemset/problem/1217/D) | CF 2100 | Ориентированный цикл: DFS с цветами 0/1/2 и обратные рёбра |
| 9 | `Extra` | [CF 915D - Almost Acyclic Graph](https://codeforces.com/problemset/problem/915/D) | CF 2200 | Ориентированный цикл и удаление одного ребра-кандидата |
| 10 | `Extra` | [CF 118E - Bertown roads](https://codeforces.com/problemset/problem/118/E) | CF 2000 | Bridges + ориентация рёбер DFS-порядком |
| 11 | `Extra` | [CF 652E - Pursuit For Artifacts](https://codeforces.com/problemset/problem/652/E) | CF 2300 | Bridge tree + агрегат наличия специального ребра на пути |

<a id="practice-dsu-mst"></a>

## 27. DSU, MST и офлайн-связность

Этап **B**. Core: **6**. Extra: **3**. Теория и признаки распознавания: [ROADMAP: DSU и MST](ROADMAP.md#topic-dsu-mst).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 1584 - Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | LC Medium | Minimum spanning tree |
| 2 | `Core` | [LC 721 - Accounts Merge](https://leetcode.com/problems/accounts-merge/) | LC Medium | DSU по общим ключам |
| 3 | `Core` | [ACMP 142 - Минимальный каркас](https://acmp.ru/index.asp?main=task&id_task=142) | - | Минимальный остов: базовая реализация Kruskal |
| 4 | `Core` | [CF 1167C - News Distribution](https://codeforces.com/problemset/problem/1167/C) | CF 1400 | DSU: массовые union и размер компоненты |
| 5 | `Core` | [CF 1213G - Path Queries](https://codeforces.com/problemset/problem/1213/G) | CF 1800 | Offline activation по весу + DSU metadata |
| 6 | `Core` | [CF 1245D - Shichikuji and Power Grid](https://codeforces.com/problemset/problem/1245/D) | CF 1900 | Prim на дополненном графе + восстановление объектов |
| 7 | `Extra` | [CF 25D - Roads not only in Berland](https://codeforces.com/problemset/problem/25/D) | CF 1900 | DSU: лишние рёбра и соединение компонент |
| 8 | `Extra` | [CF 566D - Restructuring Company](https://codeforces.com/problemset/problem/566/D) | CF 1900 | DSU-next для пропуска обработанных индексов диапазона |
| 9 | `Extra` | [CF 160D - Edges in MST](https://codeforces.com/problemset/problem/160/D) | CF 2300 | Kruskal по группам веса + bridges во временном графе |

<a id="practice-advanced-dp"></a>

## 28. DP по отрезкам, решёткам, графам и деревьям

Этап **B**. Core: **6**. Extra: **4**. Теория и признаки распознавания: [ROADMAP: продвинутое DP](ROADMAP.md#topic-advanced-dp).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 312 - Burst Balloons](https://leetcode.com/problems/burst-balloons/) | LC Hard | Interval DP |
| 2 | `Core` | [LC 337 - House Robber III](https://leetcode.com/problems/house-robber-iii/) | LC Medium | Tree DP |
| 3 | `Core` | [CF 1528A - Parsa's Humongous Tree](https://codeforces.com/problemset/problem/1528/A) | CF 1600 | Tree DP с двумя состояниями вершины |
| 4 | `Core` | [CF 1695C - Zero Path](https://codeforces.com/problemset/problem/1695/C) | CF 1700 | Grid DP по минимуму и максимуму достижимой суммы |
| 5 | `Core` | [CF 607B - Zuma](https://codeforces.com/problemset/problem/607/B) | CF 1900 | Interval DP с удалением совпадающих концов |
| 6 | `Core` | [CF 721C - Journey](https://codeforces.com/problemset/problem/721/C) | CF 1800 | DAG DP + parent + восстановление пути |
| 7 | `Extra` | [CF 225C - Barcode](https://codeforces.com/problemset/problem/225/C) | CF 1700 | DP по префиксу колонок и длине одноцветного блока |
| 8 | `Extra` | [CF 1517D - Explorer Space](https://codeforces.com/problemset/problem/1517/D) | CF 1800 | Многослойный grid DP на точное число шагов |
| 9 | `Extra` | [CF 161D - Distance in Tree](https://codeforces.com/problemset/problem/161/D) | CF 1800 | Tree DP по расстояниям и объединение детей |
| 10 | `Extra` | [CF 1092F - Tree with Maximum Cost](https://codeforces.com/problemset/problem/1092/F) | CF 1900 | Rerooting: перенос взвешенной суммы по ребру |

<a id="practice-subset-dp"></a>

## 29. DP по подмножествам, цифрам и профилю

Этап **B**. Core: **6**. Extra: **3**. Теория и признаки распознавания: [ROADMAP: subset/digit/profile DP](ROADMAP.md#topic-subset-dp).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 464 - Can I Win](https://leetcode.com/problems/can-i-win/) | LC Medium | Game DP по подмножествам |
| 2 | `Core` | [LC 902 - Numbers At Most N Given Digit Set](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/) | LC Hard | Digit DP |
| 3 | `Core` | [CF 1036C - Classy Numbers](https://codeforces.com/problemset/problem/1036/C) | CF 1900 | Digit DP: position/tight/started и ограничение числа цифр |
| 4 | `Core` | [CF 580D - Kefa and Dishes](https://codeforces.com/problemset/problem/580/D) | CF 1800 | Subset DP: dp[mask][last] |
| 5 | `Core` | [CF 165E - Compatible Numbers](https://codeforces.com/problemset/problem/165/E) | CF 2200 | SOS DP по подмаскам для совместимой маски |
| 6 | `Core` | [CF 1391D - 505](https://codeforces.com/problemset/problem/1391/D) | CF 2000 | Profile DP по маскам соседних столбцов |
| 7 | `Extra` | [CF 8C - Looking for Order](https://codeforces.com/problemset/problem/8/C) | CF 2000 | Subset DP по парам + восстановление ответа |
| 8 | `Extra` | [CF 628D - Magic Numbers](https://codeforces.com/problemset/problem/628/D) | CF 2200 | Digit DP с tight, modulo и позиционным ограничением |
| 9 | `Extra` | [CF 55D - Beautiful numbers](https://codeforces.com/problemset/problem/55/D) | CF 2500 | Digit DP с состоянием LCM ненулевых цифр |

<a id="practice-treap"></a>

## 30. Декартово дерево, treap и порядковые структуры

Этап **B**. Core: **5**. Extra: **5**. Теория и признаки распознавания: [ROADMAP: treap](ROADMAP.md#topic-treap).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [Локальный checkpoint: explicit treap](templates/java/README.md#template-treap-multiset) | Checkpoint | Split/merge по ключу, insert/erase, размер поддерева и k-я порядковая статистика |
| 2 | `Core` | [Локальный checkpoint: implicit treap](templates/java/README.md#template-implicit-treap) | Checkpoint | Split по позиции, merge, разворот диапазона и агрегат динамической последовательности |
| 3 | `Core` | [CF Gym 102787A - Shandom Ruffle](https://codeforces.com/gym/102787/problem/A) | - | Implicit treap: split/merge и перестановка блоков |
| 4 | `Core` | [CF Gym 102787E - Sneetches and Speeches 2](https://codeforces.com/gym/102787/problem/E) | - | Implicit treap: lazy flip/reverse и агрегаты непрерывного блока |
| 5 | `Core` | [CF 706D - Vasiliy's Multiset](https://codeforces.com/problemset/problem/706/D) | CF 1800 | Bitwise trie: insert/erase/max XOR |
| 6 | `Extra` | [LC 315 - Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | LC Hard | Order statistics/Fenwick |
| 7 | `Extra` | [LC 327 - Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/) | LC Hard | Prefix sums + merge-sort counting |
| 8 | `Extra` | [CF Gym 102787B - Pear TreaP](https://codeforces.com/gym/102787/problem/B) | - | Implicit treap + динамическая строка + двусторонние хеши |
| 9 | `Extra` | [CF 702F - T-Shirts](https://codeforces.com/problemset/problem/702/F) | CF 2800 | Treap/BST с агрегатами и lazy-изменениями |
| 10 | `Extra` | [CF 1748E - Yet Another Array Counting Problem](https://codeforces.com/problemset/problem/1748/E) | CF 2300 | Cartesian tree + DP по поддеревьям |

<a id="practice-flows-matching"></a>

## 31. Потоки и паросочетания

Этап **B**. Core: **4**. Extra: **5**. Теория и признаки распознавания: [ROADMAP: потоки](ROADMAP.md#topic-flows-matching).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 1820 - Maximum Number of Accepted Invitations](https://leetcode.com/problems/maximum-number-of-accepted-invitations/) | LC Medium | Kuhn bipartite matching |
| 2 | `Core` | [CF 120H - Brevity is Soul of Wit](https://codeforces.com/problemset/problem/120/H) | CF 1800 | Двудольная модель и увеличивающие пути Куна |
| 3 | `Core` | [CF 546E - Soldier and Traveling](https://codeforces.com/problemset/problem/546/E) | CF 2100 | Dinic и восстановление матрицы назначений |
| 4 | `Core` | [CF 237E - Build String](https://codeforces.com/problemset/problem/237/E) | CF 2000 | Min-cost max-flow: ограниченные ресурсы и цена единицы потока |
| 5 | `Extra` | [LC 1066 - Campus Bikes II](https://leetcode.com/problems/campus-bikes-ii/) | LC Medium | Assignment DP по маскам |
| 6 | `Extra` | [CF 1423B - Valuable Paper](https://codeforces.com/problemset/problem/1423/B) | CF 1900 | Hopcroft-Karp + binary search по допустимому порогу |
| 7 | `Extra` | [CF 1666L - Labyrinth](https://codeforces.com/problemset/problem/1666/L) | CF 1800 | Два внутренне вершинно непересекающихся ориентированных пути |
| 8 | `Extra` | [CF 510E - Fox And Dinner](https://codeforces.com/problemset/problem/510/E) | CF 2300 | Flow/matching + восстановление циклов |
| 9 | `Extra` | [CF 1082G - Petya and Graph](https://codeforces.com/problemset/problem/1082/G) | CF 2400 | Maximum closure как min-cut |

<a id="practice-advanced-strings"></a>

## 32. Ахо-Корасик, Манакер, suffix array/automaton

Этап **B**. Core: **6**. Extra: **4**. Теория и признаки распознавания: [ROADMAP: продвинутые строки](ROADMAP.md#topic-advanced-strings).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 1044 - Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/) | LC Hard | Двоичный поиск + rolling hash/suffix structure |
| 2 | `Core` | [LC 336 - Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/) | LC Hard | Trie/hash для палиндромных пар |
| 3 | `Core` | [CF 1202E - You Are Given Some Strings...](https://codeforces.com/problemset/problem/1202/E) | CF 2400 | Aho-Corasick и агрегация совпадений |
| 4 | `Core` | [CF 1326D2 - Prefix-Suffix Palindrome (Hard version)](https://codeforces.com/problemset/problem/1326/D2) | CF 1800 | Manacher для палиндрома после общего prefix/suffix |
| 5 | `Core` | [CF 514C - Watto and Mechanism](https://codeforces.com/problemset/problem/514/C) | CF 2000 | Trie с одним допустимым несовпадением |
| 6 | `Core` | [CF 19C - Deletion of Repeats](https://codeforces.com/problemset/problem/19/C) | CF 2200 | Suffix array/LCP для поиска повторяющихся блоков |
| 7 | `Extra` | [ACMP 70 - Степень строки](https://acmp.ru/index.asp?main=task&id_task=70) | - | Границы и период строки как база suffix-структур |
| 8 | `Extra` | [CF 123D - String](https://codeforces.com/problemset/problem/123/D) | CF 2300 | Suffix array + LCP + монотонная агрегация |
| 9 | `Extra` | [CF 710F - String Set Queries](https://codeforces.com/problemset/problem/710/F) | CF 2400 | Динамический набор Aho-Corasick через логарифмические объединения |
| 10 | `Extra` | [CF 873F - Forbidden Indices](https://codeforces.com/problemset/problem/873/F) | CF 2400 | Suffix automaton + агрегация по suffix links |

<a id="practice-advanced-trees"></a>

## 33. HLD, центроидная декомпозиция, small-to-large и rerooting

Этап **B**. Core: **5**. Extra: **4**. Теория и признаки распознавания: [ROADMAP: продвинутые деревья](ROADMAP.md#topic-advanced-trees).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 834 - Sum of Distances in Tree](https://leetcode.com/problems/sum-of-distances-in-tree/) | LC Hard | Rerooting |
| 2 | `Core` | [LC 1483 - Kth Ancestor of a Tree Node](https://leetcode.com/problems/kth-ancestor-of-a-tree-node/) | LC Hard | Binary lifting |
| 3 | `Core` | [CF 321C - Ciel the Commander](https://codeforces.com/problemset/problem/321/C) | CF 2100 | Построение centroid decomposition |
| 4 | `Core` | [CF 600E - Lomsat gelral](https://codeforces.com/problemset/problem/600/E) | CF 2300 | DSU-on-tree/small-to-large по частотам цветов |
| 5 | `Core` | [CF 593D - Happy Tree Party](https://codeforces.com/problemset/problem/593/D) | CF 2400 | HLD + segment tree на путях |
| 6 | `Extra` | [CF 1324F - Maximum White Subtree](https://codeforces.com/problemset/problem/1324/F) | CF 1800 | Базовый rerooting с переносом лучшей суммы |
| 7 | `Extra` | [CF 1187E - Tree Painting](https://codeforces.com/problemset/problem/1187/E) | CF 2100 | Rerooting с переносом ответа по ребру |
| 8 | `Extra` | [CF 342E - Xenia and Tree](https://codeforces.com/problemset/problem/342/E) | CF 2400 | Centroid decomposition для динамического множества |
| 9 | `Extra` | [CF 375D - Tree and Queries](https://codeforces.com/problemset/problem/375/D) | CF 2400 | DSU-on-tree по частотам цветов в поддеревьях |

<a id="practice-games"></a>

## 34. Теория игр: выигрыш/проигрыш, Nim и Sprague-Grundy

Этап **B**. Core: **6**. Extra: **3**. Теория и признаки распознавания: [ROADMAP: теория игр](ROADMAP.md#topic-games).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 292 - Nim Game](https://leetcode.com/problems/nim-game/) | LC Easy | Nim-инвариант |
| 2 | `Core` | [LC 486 - Predict the Winner](https://leetcode.com/problems/predict-the-winner/) | LC Medium | Minimax/game DP |
| 3 | `Core` | [CF 1527B1 - Palindrome Game (easy version)](https://codeforces.com/problemset/problem/1527/B1) | CF 1200 | Формальная классификация win/lose по инварианту состояния |
| 4 | `Core` | [CF 1033C - Permutation Game](https://codeforces.com/problemset/problem/1033/C) | CF 1600 | Win/lose DP на DAG состояний |
| 5 | `Core` | [CF 15C - Industrial Nim](https://codeforces.com/problemset/problem/15/C) | CF 2000 | Nim и xor-sum куч, заданных диапазонами |
| 6 | `Core` | [CF 768E - Game of Stones](https://codeforces.com/problemset/problem/768/E) | CF 2100 | Sprague-Grundy, mex и XOR независимых компонент |
| 7 | `Extra` | [CF 455B - A Lot of Games](https://codeforces.com/problemset/problem/455/B) | CF 1900 | Два win/lose-состояния на trie |
| 8 | `Extra` | [CF 786A - Berzerk](https://codeforces.com/problemset/problem/786/A) | CF 2000 | Retrograde-анализ Win/Lose/Loop в циклическом графе |
| 9 | `Extra` | [CF 850C - Arpa and a game with Mojtaba](https://codeforces.com/problemset/problem/850/C) | CF 2200 | Sprague-Grundy по маскам степеней простых |

<a id="practice-meet-in-the-middle"></a>

## 35. Meet-in-the-middle и разбиение пространства поиска

Этап **B**. Core: **4**. Extra: **4**. Теория и признаки распознавания: [ROADMAP: meet-in-the-middle](ROADMAP.md#topic-meet-in-the-middle).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 1755 - Closest Subsequence Sum](https://leetcode.com/problems/closest-subsequence-sum/) | LC Hard | Meet-in-the-middle subset sums |
| 2 | `Core` | [CF 888E - Maximum Subsequence](https://codeforces.com/problemset/problem/888/E) | CF 1800 | Две половины subset sums + поиск дополнения |
| 3 | `Core` | [CF 1006F - Xor-Paths](https://codeforces.com/problemset/problem/1006/F) | CF 2100 | Meet-in-the-middle по средней диагонали пути |
| 4 | `Core` | [CF 525E - Anya and Cubes](https://codeforces.com/problemset/problem/525/E) | CF 2100 | Троичный перебор половин + подсчёт дополнений |
| 5 | `Extra` | [CF 1105E - Helping Hiasat](https://codeforces.com/problemset/problem/1105/E) | CF 2200 | MITM для maximum independent set при n≈40 |
| 6 | `Extra` | [CF 912E - Prime Gift](https://codeforces.com/problemset/problem/912/E) | CF 2400 | MITM по группам простых + поиск k-го произведения |
| 7 | `Extra` | [CF 585D - Lizard Era: Beginning](https://codeforces.com/problemset/problem/585/D) | CF 2300 | MITM с восстановлением выбранных решений |
| 8 | `Extra` | [CF 1257F - Make Them Similar](https://codeforces.com/problemset/problem/1257/F) | CF 2400 | Разбиение пространства битов + hash векторов расстояний |

<a id="practice-sqrt-mo"></a>

## 36. Корневая декомпозиция, Mo и офлайн-запросы

Этап **C**. Core: **3**. Extra: **4**. Теория и признаки распознавания: [ROADMAP: sqrt и Mo](ROADMAP.md#topic-sqrt-mo).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: sqrt decomposition | Checkpoint | Point update и range sum по блокам; проверить границы и последний неполный блок |
| 2 | `Core` | [CF 220B - Little Elephant and Array](https://codeforces.com/problemset/problem/220/B) | CF 1800 | Mo: add/remove и частотный инвариант freq[x]=x |
| 3 | `Core` | [CF 86D - Powerful array](https://codeforces.com/problemset/problem/86/D) | CF 2200 | Mo с нелинейным вкладом значения |
| 4 | `Extra` | [LC 493 - Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) | LC Hard | Подсчёт пар через merge sort |
| 5 | `Extra` | [CF 617E - XOR and Favorite Number](https://codeforces.com/problemset/problem/617/E) | CF 2200 | Mo по массиву prefix XOR |
| 6 | `Extra` | [CF 13E - Holes](https://codeforces.com/problemset/problem/13/E) | CF 2700 | Sqrt decomposition с point updates и jump-агрегатами |
| 7 | `Extra` | [CF 455D - Serega and Fun](https://codeforces.com/problemset/problem/455/D) | CF 2700 | Динамическая последовательность в блоках + частоты |

<a id="practice-rollback-persistence"></a>

## 37. Rollback, персистентность и динамическая связность

Этап **C**. Core: **4**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: rollback и persistence](ROADMAP.md#topic-rollback-persistence).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 1146 - Snapshot Array](https://leetcode.com/problems/snapshot-array/) | LC Medium | Версии состояния массива |
| 2 | `Core` | [CF 707D - Persistent Bookcase](https://codeforces.com/problemset/problem/707/D) | CF 2200 | Дерево версий + DFS + ручной rollback изменений |
| 3 | `Core` | [CF 813E - Army Creation](https://codeforces.com/problemset/problem/813/E) | CF 2200 | Persistent segment tree по предыдущим вхождениям |
| 4 | `Core` | [CF 1140F - Extending Set of Points](https://codeforces.com/problemset/problem/1140/F) | CF 2600 | Segment tree over time + rollback DSU |
| 5 | `Extra` | [CF 891C - Envy](https://codeforces.com/problemset/problem/891/C) | CF 2300 | Rollback DSU внутри групп одинакового веса |
| 6 | `Extra` | [CF 484E - Sign on Fence](https://codeforces.com/problemset/problem/484/E) | CF 2500 | Версии persistent segment tree по порогу |

<a id="practice-dp-optimizations"></a>

## 38. Оптимизации DP: CHT/Li Chao, divide-and-conquer, Knuth

Этап **C**. Core: **5**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: оптимизации DP](ROADMAP.md#topic-dp-optimizations).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 410 - Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) | LC Hard | DP разбиений и поиск по ответу |
| 2 | `Core` | [CF 319C - Kalila and Dimna in the Logging Industry](https://codeforces.com/problemset/problem/319/C) | CF 2100 | Monotone CHT для линейного перехода DP |
| 3 | `Core` | [CF 660F - Bear and Bowling 4](https://codeforces.com/problemset/problem/660/F) | CF 2500 | Li Chao Tree для запросов в немонотонных координатах |
| 4 | `Core` | [CF 868F - Yet Another Minimization Problem](https://codeforces.com/problemset/problem/868/F) | CF 2500 | Divide-and-conquer optimization с подвижной стоимостью |
| 5 | `Core` | [CF Gym 100212C - Order-Preserving Codes](https://codeforces.com/gym/100212/attachments/download/1727/20042005-winter-petrozavodsk-camp-andrew-stankevich-contest-10-en.pdf#page=4) ; [регистрация/отправка](https://codeforces.com/gym/100212) | - | Knuth optimization и границы оптимального разбиения |
| 6 | `Extra` | [CF 932F - Escape Through Leaf](https://codeforces.com/problemset/problem/932/F) | CF 2700 | Tree DP + Li Chao/small-to-large |

<a id="practice-linear-algebra-fft"></a>

## 39. Матрицы, линейная алгебра, FFT/NTT

Этап **C**. Core: **6**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: линейная алгебра и FFT](ROADMAP.md#topic-linear-algebra-fft).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 509 - Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | LC Easy | Линейная рекуррентность |
| 2 | `Core` | [LC 43 - Multiply Strings](https://leetcode.com/problems/multiply-strings/) | LC Medium | Умножение больших чисел как база convolution |
| 3 | `Core` | [CF 222E - Decoding Genome](https://codeforces.com/problemset/problem/222/E) | CF 1900 | Матричное возведение автомата переходов |
| 4 | `Core` | [ACMP 198 - Система линейных уравнений](https://acmp.ru/index.asp?main=task&id_task=198) | - | Плотный метод Гаусса с выбором ведущего элемента |
| 5 | `Core` | [CF 1101G - (Zero XOR Subset)-less](https://codeforces.com/problemset/problem/1101/G) | CF 2300 | XOR basis как Gauss над GF(2) |
| 6 | `Core` | [CF 1096G - Lucky Tickets](https://codeforces.com/problemset/problem/1096/G) | CF 2400 | Polynomial exponentiation через FFT/NTT |
| 7 | `Extra` | [CF 528D - Fuzzy Search](https://codeforces.com/problemset/problem/528/D) | CF 2500 | Несколько convolution для неточного сопоставления строк |

<a id="practice-probability-interactive"></a>

## 40. Вероятность, рандомизация, interactive и output-only

Этап **C**. Core: **6**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: probability и interactive](ROADMAP.md#topic-probability-interactive).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 528 - Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/) | LC Medium | Случайный выбор по префиксным весам |
| 2 | `Core` | [CF 839C - Journey](https://codeforces.com/problemset/problem/839/C) | CF 1500 | Линейность ожидания и вероятностный DFS на дереве |
| 3 | `Core` | [CF 869E - The Untended Antiquity](https://codeforces.com/problemset/problem/869/E) | CF 2400 | Randomized hashing множества активных прямоугольников |
| 4 | `Core` | [CF 148D - Bag of mice](https://codeforces.com/problemset/problem/148/D) | CF 1800 | Probability DP по состояниям количества объектов |
| 5 | `Core` | [CF 1114E - Arithmetic Progression](https://codeforces.com/problemset/problem/1114/E) | CF 2200 | Randomized sampling внутри interactive-протокола |
| 6 | `Core` | [Локальный checkpoint: output-only с checker МОШ](contests/14-moscow/2025-2026/final/full-with-answers-checkers.zip) | Checkpoint | Выбрать A, C или E; получить валидное решение, проверить checker локально и только затем улучшать score |
| 7 | `Extra` | [CF 453A - Little Pony and Expected Maximum](https://codeforces.com/problemset/problem/453/A) | CF 1600 | Ожидание максимума через CDF/tail probabilities |
