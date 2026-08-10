# Банк задач

Этот каталог построен под календарь `лето -> отборы в октябре-ноябре -> финалы в марте-апреле`. Внутри каждой темы
задачи уже расположены в учебном порядке: от первого знакомства с приемом до более сложного переноса идеи.

## Объём и маршрут

- этап A0: **42 Core** и **27 Extra** - инженерная и алгоритмическая база;
- этап A1: **147 Core** и **142 Extra** - основные переносимые олимпиадные паттерны;
- этап B: **115 Core** и **45 Extra** - регулярный финальный слой;
- этап C: **60 Core** и **18 Extra** - выборочная продвинутая практика;
- сквозные темы A1/B: **30 Core** и **27 Extra**;
- полный каталог: **394 Core** и **259 Extra**, всего **653** строки;
- задачи внешних онлайн-судей: **581**, включая **61** задачу LeetCode;
- локальные checkpoints: **67**; еще **5** строк используют официальные архивы олимпиад из `contests/`.

`Core` - основной маршрут: эти задачи нужно решить все и по порядку. Если задача уже знакома, ее все равно полезно
быстро перерешать и восстановить реализацию без старого кода. `Extra` - расширение темы после Core: его брать по
обнаруженным пробелам, для дополнительного закрепления или после прохождения отборов.

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

| N | Приоритет | Задача | Сложность | Паттерн |
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

<a id="practice-bruteforce-enumeration"></a>

## Модуль 2. Полный перебор

### 2.1. Полный перебор пространства вариантов

Этап **A0**. Core: **4**. Extra: **6**. Теория и признаки распознавания: [ROADMAP: полный перебор](ROADMAP.md#topic-bruteforce-enumeration).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 78 - Subsets](https://leetcode.com/problems/subsets/) | LC Medium | Перебор всех подмножеств битовой маской или рекурсией |
| 2 | `Core` | [LC 46 - Permutations](https://leetcode.com/problems/permutations/) | LC Medium | Перебор всех перестановок без повторов |
| 3 | `Core` | [CF 214A - System of Equations](https://codeforces.com/problemset/problem/214/A) | CF 800 | Полный перебор малого диапазона двух переменных |
| 4 | `Core` | [CF 1097B - Petr and a Combination Lock](https://codeforces.com/problemset/problem/1097/B) | CF 1200 | Перебор `2^n` вариантов выбора знака |
| 5 | `Extra` | [CF 271A - Beautiful Year](https://codeforces.com/problemset/problem/271/A) | CF 800 | Последовательный перебор до первого допустимого объекта |
| 6 | `Extra` | [CF 122A - Lucky Division](https://codeforces.com/problemset/problem/122/A) | CF 1000 | Перебор небольшого заранее ограниченного семейства |
| 7 | `Extra` | [CF 479A - Expression](https://codeforces.com/problemset/problem/479/A) | CF 1000 | Перебор фиксированного числа вариантов формулы |
| 8 | `Extra` | [CF 1108C - Nice Garland](https://codeforces.com/problemset/problem/1108/C) | CF 1300 | Перебор перестановок малого алфавита |
| 9 | `Extra` | [CF 124B - Permutations](https://codeforces.com/problemset/problem/124/B) | CF 1400 | Полный перебор `n!` перестановок |
| 10 | `Extra` | [CF 550B - Preparing Olympiad](https://codeforces.com/problemset/problem/550/B) | CF 1400 | Перебор подмножеств с несколькими ограничениями |

<a id="practice-backtracking"></a>

### 2.2. Backtracking, rollback и безопасные отсечения

Этап **A0**. Core: **2**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: backtracking](ROADMAP.md#topic-backtracking).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [ACMP 101 - Магараджа](https://acmp.ru/index.asp?main=task&id_task=101) | - | Backtracking с изменением и полным откатом состояния |
| 2 | `Core` | Локальный checkpoint: backtracking с pruning | Checkpoint | Построить допустимую расстановку; проверить `apply/undo` и отсечение по доказанной верхней границе |

<a id="practice-sorting-comparators"></a>

## Модуль 3. Сортировка и порядок

### 3.1. Сравнительная сортировка, компараторы и восстановление порядка

Этап **A0**. Core: **4**. Extra: **3**. Теория и признаки распознавания: [ROADMAP: сортировка и компараторы](ROADMAP.md#topic-sorting-comparators).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 912 - Sort an Array](https://leetcode.com/problems/sort-an-array/) | LC Medium | Реализация сравнительной сортировки и проверка сложности |
| 2 | `Core` | [LC 56 - Merge Intervals](https://leetcode.com/problems/merge-intervals/) | LC Medium | Сортировка интервалов и необратимая обработка слева направо |
| 3 | `Core` | [ACMP 119 - Сортировка времени](https://acmp.ru/index.asp?main=task&id_task=119) | - | Comparator по составному ключу |
| 4 | `Core` | [CF 166A - Rank List](https://codeforces.com/problemset/problem/166/A) | CF 1100 | Несколько ключей, tie-break и блок равных элементов |
| 5 | `Extra` | [CF 1849B - Monsters](https://codeforces.com/problemset/problem/1849/B) | CF 1000 | Comparator по вычисляемому ключу и исходному индексу |
| 6 | `Extra` | [CF 1399A - Remove Smallest](https://codeforces.com/problemset/problem/1399/A) | CF 800 | После сортировки достаточно проверить соседние элементы |
| 7 | `Extra` | [CF 337A - Puzzles](https://codeforces.com/problemset/problem/337/A) | CF 900 | Минимальный диапазон в отсортированном окне |

<a id="practice-integer-sorting"></a>

### 3.2. Counting sort и radix sort

Этап **A0**. Core: **2**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: integer sorting](ROADMAP.md#topic-integer-sorting).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [ACMP 41 - Сортировка подсчетом](https://acmp.ru/index.asp?main=task&id_task=41) | - | Counting sort на малом диапазоне целых ключей |
| 2 | `Core` | Локальный checkpoint: стабильный radix sort | Checkpoint | LSD radix sort по разрядам с устойчивым counting pass и проверкой против `Arrays.sort` |

<a id="practice-coordinate-compression"></a>

### 3.3. Сжатие координат

Этап **A0**. Core: **2**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: сжатие координат](ROADMAP.md#topic-coordinate-compression).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 1331 - Rank Transform of an Array](https://leetcode.com/problems/rank-transform-of-an-array/) | LC Easy | `sorted unique` и одинаковый ранг для дубликатов |
| 2 | `Core` | [CF 978F - Mentors](https://codeforces.com/problemset/problem/978/F) | CF 1500 | Ранги с дублями и возврат ответа к исходным индексам |

<a id="practice-hash-containers"></a>

## Модуль 4. Ассоциативные контейнеры

### 4.1. Частоты, HashMap, HashSet и канонические ключи

Этап **A0**. Core: **6**. Extra: **8**. Теория и признаки распознавания: [ROADMAP: hash-контейнеры](ROADMAP.md#topic-hash-containers).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 1 - Two Sum](https://leetcode.com/problems/two-sum/) | LC Easy | HashMap: искать дополнение до добавления текущего элемента |
| 2 | `Core` | [LC 49 - Group Anagrams](https://leetcode.com/problems/group-anagrams/) | LC Medium | Группировка по каноническому ключу |
| 3 | `Core` | [ACMP 82 - Пересечение множеств](https://acmp.ru/index.asp?main=task&id_task=82) | - | Set membership и удаление дубликатов |
| 4 | `Core` | [CF 4C - Registration System](https://codeforces.com/problemset/problem/4/C) | CF 1300 | Проверка ключа и обновление счетчика |
| 5 | `Core` | [CF 1520D - Same Differences](https://codeforces.com/problemset/problem/1520/D) | CF 1200 | Подсчет пар по преобразованному ключу |
| 6 | `Core` | Локальный checkpoint: hash-контейнеры Java | Checkpoint | Частоты, set membership, составной `long` key и выбор массива вместо map |
| 7 | `Extra` | [CF 1703B - ICPC Balloons](https://codeforces.com/problemset/problem/1703/B) | CF 800 | HashSet первого появления |
| 8 | `Extra` | [CF 1722C - Word Game](https://codeforces.com/problemset/problem/1722/C) | CF 800 | Частоты строк между несколькими наборами |
| 9 | `Extra` | [CF 1955B - Progressive Square](https://codeforces.com/problemset/problem/1955/B) | CF 1000 | Сравнение мультимножеств через частоты |
| 10 | `Extra` | [ACMP 816 - Система пересекающихся множеств](https://acmp.ru/index.asp?main=task&id_task=816) | - | Двусторонние списки принадлежности множествам |
| 11 | `Extra` | [CF 1108B - Divisors of Two Integers](https://codeforces.com/problemset/problem/1108/B) | CF 1100 | Мультимножество делителей через счетчики |
| 12 | `Extra` | [CF 141A - Amusing Joke](https://codeforces.com/problemset/problem/141/A) | CF 800 | Частоты символов для сравнения мультимножеств |
| 13 | `Extra` | [CF 459B - Pashmak and Flowers](https://codeforces.com/problemset/problem/459/B) | CF 1300 | Частоты минимального и максимального значения |
| 14 | `Extra` | [CF 670C - Cinema](https://codeforces.com/problemset/problem/670/C) | CF 1300 | Частоты языков и выбор по двум критериям |

<a id="practice-ordered-set"></a>

### 4.2. Ordered set, multiset и поиск соседнего ключа

Этап **A0**. Core: **3**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: ordered set](ROADMAP.md#topic-ordered-set).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 729 - My Calendar I](https://leetcode.com/problems/my-calendar-i/) | LC Medium | `floor/ceiling` для проверки соседних интервалов |
| 2 | `Core` | [CF 1791F - Range Update Point Query](https://codeforces.com/problemset/problem/1791/F) | CF 1500 | `ceiling` и удаление следующего еще активного индекса |
| 3 | `Core` | Локальный checkpoint: ordered multiset | Checkpoint | `TreeMap<value,count>`, соседние запросы, удаление последней копии и pair-key с уникальным id |

<a id="practice-stack"></a>

## Модуль 5. Линейные контейнеры

### 5.1. Стек: вложенность и потоковая редукция

Этап **A0**. Core: **3**. Extra: **3**. Теория и признаки распознавания: [ROADMAP: стек](ROADMAP.md#topic-stack).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 20 - Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | LC Easy | Стек незакрытых конструкций |
| 2 | `Core` | [CF 1907B - YetnotherrokenKeoard](https://codeforces.com/problemset/problem/1907/B) | CF 1000 | Два стека индексов и восстановление исходного порядка |
| 3 | `Core` | [CF 1428C - ABBB](https://codeforces.com/problemset/problem/1428/C) | CF 1100 | Потоковая редукция через вершину стека |
| 4 | `Extra` | [ACMP 899 - Баланс скобок](https://acmp.ru/index.asp?main=task&id_task=899) | - | Несколько типов скобок и строгая вложенность |
| 5 | `Extra` | [CF 797C - Minimal string](https://codeforces.com/problemset/problem/797/C) | CF 1700 | Стек-буфер плюс минимум необработанного суффикса |
| 6 | `Extra` | Локальный checkpoint: стек на primitive array | Checkpoint | Реализовать стек индексов без boxing и проверить пустое состояние |

<a id="practice-queue"></a>

### 5.2. FIFO-очередь

Этап **A0**. Core: **1**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: FIFO-очередь](ROADMAP.md#topic-queue).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 1234B2 - Social Network](https://codeforces.com/problemset/problem/1234/B2) | CF 1300 | Ограниченная FIFO-очередь плюс множество присутствующих элементов |

<a id="practice-deque"></a>

### 5.3. Обычный deque и lazy deletion с концов

Этап **A0**. Core: **2**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: deque](ROADMAP.md#topic-deque).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 1579E1 - Permutation Minimization by Deque](https://codeforces.com/problemset/problem/1579/E1) | CF 1000 | Выбор `addFirst` или `addLast` при построении последовательности |
| 2 | `Core` | Локальный checkpoint: расписание станков | Checkpoint | Обычные и срочные задачи входят с разных концов; отмененные элементы удаляются лениво |

<a id="practice-priority-queue-extremum"></a>

## Модуль 6. Priority queue

### 6.1. Динамический экстремум, best-first processing и scheduling

Этап **A0**. Core: **4**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: динамический экстремум](ROADMAP.md#topic-priority-queue-extremum).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 1800C2 - Powering the Hero](https://codeforces.com/problemset/problem/1800/C2) | CF 1100 | Добавлять кандидатов и извлекать лучший по событию |
| 2 | `Core` | [CF Gym 102961T - Room Allocation](https://codeforces.com/gym/102961/problem/T) | - | Переиспользовать ресурс с минимальным временем освобождения |
| 3 | `Core` | [CF 1353D - Constructing the Array](https://codeforces.com/problemset/problem/1353/D) | CF 1600 | Составной приоритет: длина по убыванию, левая граница по возрастанию |
| 4 | `Core` | [CF 853A - Planning](https://codeforces.com/problemset/problem/853/A) | CF 1500 | Выбирать максимальную текущую потерю из доступных задач |

<a id="practice-bounded-heap"></a>

### 6.2. Bounded heap, top-k и remove-worst

Этап **A0**. Core: **1**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: bounded heap](ROADMAP.md#topic-bounded-heap).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 703 - Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | LC Easy | Min-heap из лучших `k`, где корень - худший из выбранных |
| 2 | `Extra` | [LC 973 - K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | LC Medium | Heap размера `k` для selection без полной сортировки |

<a id="practice-priority-queue-stale"></a>

### 6.3. Несколько порядков доступа и stale entries

Этап **A0**. Core: **1**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: stale entries](ROADMAP.md#topic-priority-queue-stale).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 1468C - Berpizza](https://codeforces.com/problemset/problem/1468/C) | CF 1700 | FIFO и max-heap над одними объектами; `served[]` и пропуск stale entries |

## Модуль 7. Префиксные преобразования

<a id="practice-prefix-1d"></a>

### 7.1. Одномерные префиксы и обратимые агрегаты

Этап **A1**. Core: **5**. Extra: **5**. Теория и признаки распознавания: [ROADMAP: одномерные префиксы](ROADMAP.md#topic-prefix-1d).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 303 - Range Sum Query Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | LC Easy | Префиксная сумма и запрос на полуинтервале |
| 2 | `Extra` | [LC 1310 - XOR Queries of a Subarray](https://leetcode.com/problems/xor-queries-of-a-subarray/) | LC Medium | Префиксный XOR в базовом интерфейсе запросов |
| 3 | `Core` | [CF EDU 10.1A - Construction of Prefix Sums](https://codeforces.com/edu/course/2/lesson/10/1/practice/contest/324365/problem/A) | EDU | Восстановление исходного массива по префиксам |
| 4 | `Core` | [CF EDU 10.2A - Sum on Segment](https://codeforces.com/edu/course/2/lesson/10/2/practice/contest/324367/problem/A) | EDU | Статическая сумма на произвольном отрезке |
| 5 | `Core` | [CF EDU 10.2B - XOR on Segment](https://codeforces.com/edu/course/2/lesson/10/2/practice/contest/324367/problem/B) | EDU | Префиксный XOR как обратимый агрегат |
| 6 | `Core` | [CF 466C - Number of Ways](https://codeforces.com/problemset/problem/466/C) | CF 1700 | Подсчет пар точек разбиения по значениям префикса |
| 7 | `Extra` | [CF 1516B - AGAGA XOOORRR](https://codeforces.com/problemset/problem/1516/B) | CF 1500 | Разбиение на сегменты с одинаковым XOR |
| 8 | `Extra` | [CF 1807D - Odd Queries](https://codeforces.com/problemset/problem/1807/D) | CF 900 | Виртуальная замена диапазона через его префиксную сумму |
| 9 | `Extra` | [CF EDU 10.4G - Maximum Sum Segment](https://codeforces.com/edu/course/2/lesson/10/4/practice/contest/324369/problem/G) | EDU | Префиксный минимум и лучший последующий префикс |
| 10 | `Extra` | [CF EDU 10.4K - Permutation Composition Queries](https://codeforces.com/edu/course/2/lesson/10/4/practice/contest/324369/problem/K) | EDU | Префиксное произведение в некоммутативной группе с обратной перестановкой |

<a id="practice-prefix-multidimensional"></a>

### 7.2. Многомерные префиксные суммы

Этап **A1**. Core: **3**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: многомерные префиксы](ROADMAP.md#topic-prefix-multidimensional).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 304 - Range Sum Query 2D Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) | LC Medium | 2D-prefix и inclusion-exclusion четырех углов |
| 2 | `Core` | [CF EDU 10.3A - Sum on Rectangle](https://codeforces.com/edu/course/2/lesson/10/3/practice/contest/324368/problem/A) | EDU | Прямоугольный запрос с аккуратными границами |
| 3 | `Core` | [CF 1722E - Counting Rectangles](https://codeforces.com/problemset/problem/1722/E) | CF 1600 | Взвешенный 2D-prefix и строгие границы координат |
| 4 | `Extra` | [CF EDU 10.3B - Sum in 5D](https://codeforces.com/edu/course/2/lesson/10/3/practice/contest/324368/problem/B) | EDU | Обобщение inclusion-exclusion на пять измерений |

<a id="practice-difference-array"></a>

### 7.3. Массив разностей для постоянной прибавки

Этап **A1**. Core: **5**. Extra: **3**. Теория и признаки распознавания: [ROADMAP: массив разностей](ROADMAP.md#topic-difference-array).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: range add offline | Checkpoint | `diff[l] += x`, `diff[r] -= x`, sentinel и восстановление на случайных полуинтервалах |
| 2 | `Core` | [CF EDU 10.4A - Add on Segment](https://codeforces.com/edu/course/2/lesson/10/4/practice/contest/324369/problem/A) | EDU | Постоянная прибавка на диапазоне и одна интеграция |
| 3 | `Core` | [CF 816B - Karen and Coffee](https://codeforces.com/problemset/problem/816/B) | CF 1400 | Разности покрытия плюс префикс по готовому предикату |
| 4 | `Core` | [CF EDU 10.4E - Greg and Array](https://codeforces.com/edu/course/2/lesson/10/4/practice/contest/324369/problem/E) | EDU | Два вложенных уровня offline difference arrays |
| 5 | `Core` | [CF EDU 10.4I - Add, Sum](https://codeforces.com/edu/course/2/lesson/10/4/practice/contest/324369/problem/I) | EDU | Range add, восстановление значений и второй префикс для range sum |
| 6 | `Extra` | [CF EDU 10.4F - Little Girl and Maximum Sum](https://codeforces.com/edu/course/2/lesson/10/4/practice/contest/324369/problem/F) | EDU | Частоты покрытия через разности плюс перестановочный greedy |
| 7 | `Extra` | [CF EDU 10.4H - High Mountains](https://codeforces.com/edu/course/2/lesson/10/4/practice/contest/324369/problem/H) | EDU | Offline suffix add при сохранении отсортированного порядка |
| 8 | `Extra` | [CF 1795C - Tea Tasting](https://codeforces.com/problemset/problem/1795/C) | CF 1500 | Разности полных вкладов плюс один частичный край |

<a id="practice-difference-arithmetic-progression"></a>

### 7.4. Разности для арифметической прогрессии

Этап **A1**. Core: **1**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: разности прогрессии](ROADMAP.md#topic-difference-arithmetic-progression).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF EDU 10.4B - Add Arithmetic Progression on Segment](https://codeforces.com/edu/course/2/lesson/10/4/practice/contest/324369/problem/B) | EDU | Вторая разность и две интеграции линейной прибавки |
| 2 | `Extra` | [CF EDU 10.4D - Pekora and Trampolines](https://codeforces.com/edu/course/2/lesson/10/4/practice/contest/324369/problem/D) | EDU | Распространение будущих линейных вкладов через разности |

<a id="practice-difference-2d"></a>

### 7.5. Двумерный массив разностей

Этап **A1**. Core: **2**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: двумерные разности](ROADMAP.md#topic-difference-2d).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF EDU 10.4C - Add on Rectangle](https://codeforces.com/edu/course/2/lesson/10/4/practice/contest/324369/problem/C) | EDU | Четыре угловых события и два восстановления |
| 2 | `Core` | Локальный checkpoint: 2D difference | Checkpoint | Случайные прибавки на прямоугольниках и stress против прямой матрицы |

<a id="practice-two-pointers-opposite"></a>

## Модуль 8. Два указателя

### 8.1. Встречные указатели

Этап **A1**. Core: **2**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: встречные указатели](ROADMAP.md#topic-two-pointers-opposite).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 11 - Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | LC Medium | Доказанное отбрасывание одного из крайних кандидатов |
| 2 | `Core` | [CF Gym 102961G - Sum of Two Values](https://codeforces.com/gym/102961/problem/G) | - | Сумма пары в отсортированном массиве с восстановлением индексов |
| 3 | `Extra` | [CF 1538C - Number of Pairs](https://codeforces.com/problemset/problem/1538/C) | CF 1300 | Линейный `count(sum <= x)` и разность двух ответов |

<a id="practice-two-pointers-merge"></a>

### 8.2. Слияние отсортированных потоков

Этап **A1**. Core: **4**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: слияние потоков](ROADMAP.md#topic-two-pointers-merge).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF EDU 9.1A - Merge Arrays](https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A) | EDU | Классическое линейное слияние двух массивов |
| 2 | `Core` | [CF EDU 9.1B - Number of Smaller](https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B) | EDU | Монотонная граница количества элементов меньше запроса |
| 3 | `Core` | [CF EDU 9.1C - Number of Equal](https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/C) | EDU | Блоки равных значений и произведение их частот |
| 4 | `Core` | [CF 489B - BerSU Ball](https://codeforces.com/problemset/problem/489/B) | CF 1200 | Greedy matching двух отсортированных потоков |
| 5 | `Extra` | [CF EDU 9.3D - Stylish Clothes](https://codeforces.com/edu/course/2/lesson/9/3/practice/contest/307094/problem/D) | EDU | Несколько отсортированных потоков и продвижение текущего минимума |

<a id="practice-two-pointers-synchronized"></a>

### 8.3. Синхронные монотонные проходы

Этап **A1**. Core: **1**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: синхронные проходы](ROADMAP.md#topic-two-pointers-synchronized).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 1036D - Vasya and Arrays](https://codeforces.com/problemset/problem/1036/D) | CF 1600 | Закрытие двух положительных блоков при равенстве сумм |
| 2 | `Extra` | [CF 1669F - Eating Candies](https://codeforces.com/problemset/problem/1669/F) | CF 1100 | Синхронизация накопленных сумм с двух концов |

<a id="practice-fixed-window"></a>

## Модуль 9. Окна и очередь с агрегатом

### 9.1. Окно фиксированной длины

Этап **A1**. Core: **1**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: фиксированное окно](ROADMAP.md#topic-fixed-window).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 1690D - Black and White Stripe](https://codeforces.com/problemset/problem/1690/D) | CF 1000 | Добавить справа, удалить вышедший слева и сравнить все окна длины `k` |
| 2 | `Extra` | [CF EDU 10.4J - Designer Solution](https://codeforces.com/edu/course/2/lesson/10/4/practice/contest/324369/problem/J) | EDU | Окно длины `k` по шкале значений и число недостающих элементов |

<a id="practice-sliding-window"></a>

### 9.2. Variable sliding window и подсчет подмассивов

Этап **A1**. Core: **8**. Extra: **9**. Теория и признаки распознавания: [ROADMAP: sliding window](ROADMAP.md#topic-sliding-window).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 3 - Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | LC Medium | Частотное окно и удаление нарушителя слева |
| 2 | `Core` | [CF EDU 9.2A - Segment with Small Sum](https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A) | EDU | Максимальное окно положительных чисел с суммой не больше `s` |
| 3 | `Core` | [CF EDU 9.2B - Segment with Big Sum](https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/B) | EDU | Минимальное окно с суммой не меньше `s` |
| 4 | `Core` | [CF EDU 9.2C - Number of Segments with Small Sum](https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/C) | EDU | Подсчет всех допустимых окончаний через длину текущего окна |
| 5 | `Core` | [CF EDU 9.2E - Segments with Small Set](https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/E) | EDU | Окно с ограничением на число различных значений |
| 6 | `Core` | [CF 701C - They Are Everywhere](https://codeforces.com/problemset/problem/701/C) | CF 1500 | Минимальное окно, покрывающее весь требуемый алфавит |
| 7 | `Core` | [CF EDU 9.3F - Card Substrings](https://codeforces.com/edu/course/2/lesson/9/3/practice/contest/307094/problem/F) | EDU | Частотные верхние границы для каждого символа |
| 8 | `Core` | [CF EDU 9.3G - Not Very Rude Substring](https://codeforces.com/edu/course/2/lesson/9/3/practice/contest/307094/problem/G) | EDU | Инкрементальное обновление числа пар внутри окна |
| 9 | `Extra` | [CF EDU 9.2D - Number of Segments with Big Sum](https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/D) | EDU | Дополнение к подсчету окон с малой суммой |
| 10 | `Extra` | [CF EDU 9.3A - Looped Playlist](https://codeforces.com/edu/course/2/lesson/9/3/practice/contest/307094/problem/A) | EDU | Циклическое окно после отделения полных оборотов |
| 11 | `Extra` | [CF EDU 9.3B - Total Length](https://codeforces.com/edu/course/2/lesson/9/3/practice/contest/307094/problem/B) | EDU | Сумма длин всех допустимых окон |
| 12 | `Extra` | [CF EDU 9.3C - City of Che](https://codeforces.com/edu/course/2/lesson/9/3/practice/contest/307094/problem/C) | EDU | Монотонная граница по расстоянию и подсчет последующих пар |
| 13 | `Extra` | [CF EDU 9.3E - Knapsack on a Segment](https://codeforces.com/edu/course/2/lesson/9/3/practice/contest/307094/problem/E) | EDU | Максимальное окно с несколькими типами ограниченного ресурса |
| 14 | `Extra` | [CF EDU 9.3H - A-B Knapsack](https://codeforces.com/edu/course/2/lesson/9/3/practice/contest/307094/problem/H) | EDU | Два связанных лимита и поддержка допустимого окна |
| 15 | `Extra` | [CF EDU 9.3I - Segment with Required Subset](https://codeforces.com/edu/course/2/lesson/9/3/practice/contest/307094/problem/I) | EDU | Окно плюс состояние достижимости требуемой суммы |
| 16 | `Extra` | [CF 580B - Kefa and Company](https://codeforces.com/problemset/problem/580/B) | CF 1500 | Сортировка по ключу плюс окно и `long`-сумма |
| 17 | `Extra` | [CF 1358D - The Best Vacation](https://codeforces.com/problemset/problem/1358/D) | CF 1900 | Циклическое взвешенное окно и частично взятый край |

<a id="practice-monotonic-deque"></a>

### 9.3. Монотонный deque для экстремума окна

Этап **A1**. Core: **3**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: монотонный deque](ROADMAP.md#topic-monotonic-deque).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 239 - Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | LC Hard | Deque индексов с убывающими значениями |
| 2 | `Core` | [CF EDU 9.2F - Segments with Small Spread](https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F) | EDU | Два монотонных deque для условия `max-min <= k` |
| 3 | `Core` | [CF 6E - Exposition](https://codeforces.com/problemset/problem/6/E) | CF 1900 | Два deque, максимальная длина и восстановление всех лучших окон |

<a id="practice-aggregate-queue"></a>

### 9.4. Очередь с агрегатом на двух стеках

Этап **B**. Core: **2**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: aggregate queue](ROADMAP.md#topic-aggregate-queue).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: aggregate queue | Checkpoint | Очередь на двух стеках с `gcd/min` каждого префикса и stress против прямого окна |
| 2 | `Core` | [CF EDU 9.2G - Coprime Segment](https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/G) | EDU | Sliding window с `gcd` всего окна через очередь с агрегатом |

<a id="practice-nearest-element-stack"></a>

## Модуль 10. Монотонный стек

### 10.1. Ближайший подходящий элемент

Этап **A1**. Core: **2**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: ближайший элемент](ROADMAP.md#topic-nearest-element-stack).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 739 - Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | LC Medium | Next greater и завершение ожидающих индексов |
| 2 | `Core` | [CF Gym 102961Z - Nearest Smaller Values](https://codeforces.com/gym/102961/problem/Z) | - | Previous strictly smaller; при равенстве требуется `pop >=` |

<a id="practice-histogram-stack"></a>

### 10.2. Область действия и гистограмма

Этап **A1**. Core: **2**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: гистограмма](ROADMAP.md#topic-histogram-stack).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 84 - Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | LC Hard | Ближайшие меньшие границы области каждой высоты |
| 2 | `Core` | [CF 547B - Mike and Feet](https://codeforces.com/problemset/problem/547/B) | CF 1900 | Span каждого минимума и распространение ответа по длинам |

<a id="practice-contribution-stack"></a>

### 10.3. Подсчет вкладов через монотонный стек

Этап **A1**. Core: **2**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: вклады монотонного стека](ROADMAP.md#topic-contribution-stack).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 907 - Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) | LC Medium | Число подмассивов, где элемент выбран минимумом |
| 2 | `Core` | [CF 817D - Imbalanced Array](https://codeforces.com/problemset/problem/817/D) | CF 1900 | Вклад элемента как максимума и минимума с асимметричными tie rules |

<a id="practice-greedy-stack"></a>

### 10.4. Greedy-удаления стеком

Этап **A1**. Core: **2**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: greedy stack](ROADMAP.md#topic-greedy-stack).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 402 - Remove K Digits](https://leetcode.com/problems/remove-k-digits/) | LC Medium | Удалять предыдущую большую цифру при ограниченном бюджете |
| 2 | `Core` | [CF 1886C - Decreasing String](https://codeforces.com/problemset/problem/1886/C) | CF 1600 | Удалять больший предыдущий символ, пока это улучшает лексикографический ответ |

<a id="practice-stack-dp"></a>

### 10.5. DP по границам монотонного стека

Этап **B**. Core: **1**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: stack DP](ROADMAP.md#topic-stack-dp).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 1313C2 - Skyscrapers](https://codeforces.com/problemset/problem/1313/C2) | CF 1900 | Clipped prefix/suffix DP и восстановление массива |

<a id="practice-sweep-events"></a>

## Модуль 11. Sweep line

### 11.1. События и счетчик покрытия

Этап **A1**. Core: **3**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: события sweep line](ROADMAP.md#topic-sweep-events).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 1000C - Covered Points Count](https://codeforces.com/problemset/problem/1000/C) | CF 1700 | Разность событий на закрытых целочисленных интервалах |
| 2 | `Core` | [CF 612D - The Union of k-Segments](https://codeforces.com/problemset/problem/612/D) | CF 1800 | Tie order событий, порог покрытия и восстановление отрезков |
| 3 | `Core` | [CF 1420D - Rescue Nibel](https://codeforces.com/problemset/problem/1420/D) | CF 1800 | Считать группу в момент открытия последнего интервала |

<a id="practice-sweep-active-set"></a>

### 11.2. Sweep line с активным ordered set

Этап **A1/B**. Core: **1**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: active set](ROADMAP.md#topic-sweep-active-set).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 1249D2 - Too Many Segments](https://codeforces.com/problemset/problem/1249/D2) | CF 1800 | Удалять активный интервал с максимальной правой границей |
| 2 | `Extra` | [CF 1284D - New Year and Conference](https://codeforces.com/problemset/problem/1284/D) | CF 2100 | Два симметричных sweep line и active multiset |

## Модуль 12. Бинарный и унимодальный поиск

<a id="practice-binary-boundaries"></a>

### 12.1. Границы в отсортированном массиве и first true

Этап **A1**. Core: **7**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: бинарные границы](ROADMAP.md#topic-binary-boundaries).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 704 - Binary Search](https://leetcode.com/problems/binary-search/) | LC Easy | Классический поиск точного значения |
| 2 | `Core` | [LC 278 - First Bad Version](https://leetcode.com/problems/first-bad-version/) | LC Easy | Чистый `first true` на монотонном предикате |
| 3 | `Core` | [LC 34 - Find First and Last Position](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | LC Medium | Два поиска: first `>= x` и first `> x` |
| 4 | `Core` | [CF EDU 6.1A - Binary Search](https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/A) | EDU | Наличие элемента и единый инвариант границ |
| 5 | `Core` | [CF EDU 6.1B - Closest to the Left](https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/B) | EDU | Последний элемент `<= x` или sentinel |
| 6 | `Core` | [CF EDU 6.1C - Closest to the Right](https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/C) | EDU | Первый элемент `>= x` или позиция за концом |
| 7 | `Core` | [CF EDU 6.1D - Fast Search](https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/D) | EDU | Две границы для числа элементов в `[l, r]` |
| 8 | `Extra` | [CF 706B - Interesting drink](https://codeforces.com/problemset/problem/706/B) | CF 1100 | Upper bound как число элементов не больше `x` |
| 9 | `Extra` | [CF 1742E - Scuza](https://codeforces.com/problemset/problem/1742/E) | CF 1200 | Upper bound по максимумам префикса плюс его сумма |

<a id="practice-binary-answer-integer"></a>

### 12.2. Целочисленный поиск по ответу

Этап **A1**. Core: **6**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: целочисленный поиск по ответу](ROADMAP.md#topic-binary-answer-integer).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 875 - Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | LC Medium | Минимальная скорость и ceiling division |
| 2 | `Core` | [CF EDU 6.2A - Packing Rectangles](https://codeforces.com/edu/course/2/lesson/6/2/practice/contest/283932/problem/A) | EDU | Минимальный размер квадрата через `first true` |
| 3 | `Core` | [CF EDU 6.2C - Very Easy Task](https://codeforces.com/edu/course/2/lesson/6/2/practice/contest/283932/problem/C) | EDU | Минимальное время производства двумя машинами |
| 4 | `Core` | [CF EDU 6.2F - String Game](https://codeforces.com/edu/course/2/lesson/6/2/practice/contest/283932/problem/F) | EDU | Максимум удалений с проверкой подпоследовательности |
| 5 | `Core` | [CF EDU 6.2G - Student Councils](https://codeforces.com/edu/course/2/lesson/6/2/practice/contest/283932/problem/G) | EDU | Максимум групп через сумму ограниченных вкладов ресурсов |
| 6 | `Core` | [CF EDU 6.2H - Hamburgers](https://codeforces.com/edu/course/2/lesson/6/2/practice/contest/283932/problem/H) | EDU | Максимум изделий при покупке недостающих ресурсов |
| 7 | `Extra` | [CF EDU 6.2D - Children Holiday](https://codeforces.com/edu/course/2/lesson/6/2/practice/contest/283932/problem/D) | EDU | Циклы работы и отдыха плюс восстановление распределения |
| 8 | `Extra` | [CF 670D1 - Magic Powder - 1](https://codeforces.com/problemset/problem/670/D1) | CF 1400 | Линейная проверка объема производства |

<a id="practice-binary-answer-real"></a>

### 12.3. Вещественный бинарный поиск

Этап **A1**. Core: **3**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: вещественный поиск](ROADMAP.md#topic-binary-answer-real).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF EDU 6.2B - Ropes](https://codeforces.com/edu/course/2/lesson/6/2/practice/contest/283932/problem/B) | EDU | Максимальная вещественная длина при целочисленном числе кусков |
| 2 | `Core` | [CF EDU 6.2E - Equation](https://codeforces.com/edu/course/2/lesson/6/2/practice/contest/283932/problem/E) | EDU | `first true` для непрерывной монотонной функции |
| 3 | `Core` | [CF EDU 6.3A - Get Together](https://codeforces.com/edu/course/2/lesson/6/3/practice/contest/285083/problem/A) | EDU | Пересечение достижимых интервалов к моменту времени |

<a id="practice-binary-minimax"></a>

### 12.4. Minimax и bottleneck feasibility

Этап **A1**. Core: **3**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: minimax feasibility](ROADMAP.md#topic-binary-minimax).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Extra` | [LC 410 - Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) | LC Hard | Тот же minimax для числа частей в другом интерфейсе |
| 2 | `Core` | [CF EDU 6.3B - Splitting an Array](https://codeforces.com/edu/course/2/lesson/6/3/practice/contest/285083/problem/B) | EDU | Минимизировать максимальную сумму блока через greedy `can(x)` |
| 3 | `Core` | [CF EDU 6.3C - Cows in Stalls](https://codeforces.com/edu/course/2/lesson/6/3/practice/contest/285083/problem/C) | EDU | Максимизировать минимальное расстояние через greedy placement |
| 4 | `Core` | [CF EDU 6.3D - Minimum Maximum on the Path](https://codeforces.com/edu/course/2/lesson/6/3/practice/contest/285083/problem/D) | EDU | Существование пути при пороге на вес ребра |
| 5 | `Extra` | [ACMP 523 - Роман в томах](https://acmp.ru/index.asp?main=task&id_task=523) | - | Разбиение последовательности и greedy-проверка порога |

<a id="practice-parametric-average"></a>

### 12.5. Параметрический поиск по среднему или отношению

Этап **B**. Core: **3**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: параметрический поиск](ROADMAP.md#topic-parametric-average).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF EDU 6.4A - Maximum Average Segment](https://codeforces.com/edu/course/2/lesson/6/4/practice/contest/285069/problem/A) | EDU | Вычитание ответа и prefix minimum |
| 2 | `Core` | [CF EDU 6.4B - Minimum Average Path](https://codeforces.com/edu/course/2/lesson/6/4/practice/contest/285069/problem/B) | EDU | Вычитание ответа и DP-проверка пути |
| 3 | `Core` | [CF EDU 6.4C - Pair Selection](https://codeforces.com/edu/course/2/lesson/6/4/practice/contest/285069/problem/C) | EDU | Максимальное отношение через преобразование суммы |

<a id="practice-binary-kth"></a>

### 12.6. K-й объект через функцию количества

Этап **B**. Core: **3**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: k-й объект](ROADMAP.md#topic-binary-kth).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF EDU 6.5A - K-th Number in the Union of Segments](https://codeforces.com/edu/course/2/lesson/6/5/practice/contest/285084/problem/A) | EDU | Первый `x`, для которого объектов `<= x` достаточно |
| 2 | `Core` | [CF EDU 6.5B - Multiplication Table](https://codeforces.com/edu/course/2/lesson/6/5/practice/contest/285084/problem/B) | EDU | Суммарный count по строкам таблицы произведений |
| 3 | `Core` | [CF EDU 6.5C - K-th Sum](https://codeforces.com/edu/course/2/lesson/6/5/practice/contest/285084/problem/C) | EDU | Count парных сумм через два указателя |

<a id="practice-unimodal-search"></a>

### 12.7. Дискретный унимодальный поиск

Этап **B**. Core: **1**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: унимодальный поиск](ROADMAP.md#topic-unimodal-search).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 1355E - Restorer Distance](https://codeforces.com/problemset/problem/1355/E) | CF 2100 | Сравнение соседних значений дискретной выпуклой стоимости |

<a id="practice-greedy-intervals"></a>

## Модуль 13. Жадные алгоритмы

### 13.1. Interval scheduling

Этап **A1**. Core: **1**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: interval scheduling](ROADMAP.md#topic-greedy-intervals).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 435 - Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | LC Medium | Выбирать следующий интервал с минимальным правым концом |

<a id="practice-greedy-local"></a>

### 13.2. Независимый локальный выбор

Этап **A1**. Core: **1**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: локальный greedy](ROADMAP.md#topic-greedy-local).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 514A - Chewbacca and Number](https://codeforces.com/problemset/problem/514/A) | CF 1200 | Независимо выбрать лучшую форму каждой цифры |
| 2 | `Extra` | [CF 34B - Sale](https://codeforces.com/problemset/problem/34/B) | CF 900 | Взять фиксированное число самых выгодных независимых объектов |
| 3 | `Extra` | [ACMP 39 - Волосатый бизнес](https://acmp.ru/index.asp?main=task&id_task=39) | - | Суффиксный максимум и доказательство момента действия |

<a id="practice-greedy-packing"></a>

### 13.3. Жадная упаковка ограниченных типов

Этап **A1**. Core: **1**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: жадная упаковка](ROADMAP.md#topic-greedy-packing).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 158B - Taxi](https://codeforces.com/problemset/problem/158/B) | CF 1100 | Сначала совместить самые крупные группы, затем заполнить остатки |

<a id="practice-greedy-frontier"></a>

### 13.4. Монотонный frontier достижимости

Этап **A1**. Core: **2**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: greedy frontier](ROADMAP.md#topic-greedy-frontier).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 55 - Jump Game](https://leetcode.com/problems/jump-game/) | LC Medium | Дальняя достижимая позиция как достаточное состояние |
| 2 | `Core` | [CF 545C - Woodcutters](https://codeforces.com/problemset/problem/545/C) | CF 1500 | Необратимая обработка объектов слева направо |
| 3 | `Extra` | [CF 230A - Dragons](https://codeforces.com/problemset/problem/230/A) | CF 1000 | Сортировка требований и рост доступного ресурса |
| 4 | `Extra` | [CF 58A - Chat room](https://codeforces.com/problemset/problem/58/A) | CF 1000 | Самый ранний возможный выбор символа подпоследовательности |

<a id="practice-greedy-scheduling"></a>

### 13.5. Scheduling, tentative selection и remove-worst

Этап **A1/B**. Core: **2**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: greedy scheduling](ROADMAP.md#topic-greedy-scheduling).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 545D - Queue](https://codeforces.com/problemset/problem/545/D) | CF 1300 | Сортировка и инвариант принятого префикса |
| 2 | `Core` | [CF 1526C2 - Potions](https://codeforces.com/problemset/problem/1526/C2) | CF 1600 | Tentative selection и удаление худшего выбранного элемента |
| 3 | `Extra` | [CF 1041C - Coffee Break](https://codeforces.com/problemset/problem/1041/C) | CF 1600 | Раскладывать события по минимальному допустимому дню |
| 4 | `Extra` | Локальный checkpoint: exchange proof | Checkpoint | Сформулировать допустимость, локальный обмен и причину, почему remove-worst сохраняет оптимум |

<a id="practice-bit-operations"></a>

## Модуль 14. Биты и маски

### 14.1. Побитовые операции и разложение числа

Этап **A1**. Core: **4**. Extra: **3**. Теория и признаки распознавания: [ROADMAP: побитовые операции](ROADMAP.md#topic-bit-operations).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: Java bit operations | Checkpoint | Set/clear/toggle/test, lowbit, `>>` и `>>>` на `int/long` |
| 2 | `Core` | [ACMP 542 - Бит-реверс](https://acmp.ru/index.asp?main=task&id_task=542) | - | Извлечение битов, сдвиги и построение результата |
| 3 | `Core` | [CF 579A - Raising Bacteria](https://codeforces.com/problemset/problem/579/A) | CF 1000 | Popcount как число степеней двойки |
| 4 | `Core` | [CF 1420B - Rock and Lever](https://codeforces.com/problemset/problem/1420/B) | CF 1200 | Группировка по старшему установленному биту |
| 5 | `Extra` | [CF 1559A - Mocha and Math](https://codeforces.com/problemset/problem/1559/A) | CF 900 | Сведение массива побитовым AND |
| 6 | `Extra` | [CF 1362C - Johnny and Another Rating Drop](https://codeforces.com/problemset/problem/1362/C) | CF 1400 | Вклад каждого младшего бита |
| 7 | `Extra` | [CF 1095C - Powers Of Two](https://codeforces.com/problemset/problem/1095/C) | CF 1400 | Расщепление степеней двойки через heap |

<a id="practice-bitmask-set"></a>

### 14.2. Битовая маска как множество

Этап **A1**. Core: **2**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: маска-множество](ROADMAP.md#topic-bitmask-set).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 1239 - Maximum Length of a Concatenated String with Unique Characters](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/) | LC Medium | Маска символов и проверка конфликтов пересечением |
| 2 | `Core` | [CF 467B - Fedor and New Game](https://codeforces.com/problemset/problem/467/B) | CF 1100 | XOR двух масок и popcount различий |

<a id="practice-submask-enumeration"></a>

### 14.3. Перебор подмасок

Этап **A1**. Core: **2**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: подмаски](ROADMAP.md#topic-submask-enumeration).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: submask iteration | Checkpoint | Перечислить все подмаски, включая ноль; проверить суммарное `O(3^n)` для всех масок |
| 2 | `Core` | [CF 1552D - Array Differentiation](https://codeforces.com/problemset/problem/1552/D) | CF 1800 | Разделение малого набора на две подмаски с равной суммой |

<a id="practice-boolean-algebra"></a>

### 14.4. Булева алгебра и побитовые ограничения

Этап **A1**. Core: **2**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: булева алгебра](ROADMAP.md#topic-boolean-algebra).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: boolean algebra | Checkpoint | Таблицы истинности, De Morgan, CNF/DNF, независимость битов и проверка формул на малых масках |
| 2 | `Core` | [CF 1395C - Boboniu and Bit Operations](https://codeforces.com/problemset/problem/1395/C) | CF 1600 | Перебирать маску ответа и проверять ограничения независимо по битам |

<a id="practice-gcd-lcm"></a>

## Модуль 15. Теория чисел

### 15.1. GCD, LCM и обработка кратных

Этап **A1**. Core: **3**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: GCD и LCM](ROADMAP.md#topic-gcd-lcm).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 1979 - Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) | LC Easy | Итеративный алгоритм Евклида |
| 2 | `Core` | [ACMP 14 - НОК](https://acmp.ru/index.asp?main=task&id_task=14) | - | `a / gcd(a,b) * b` и контроль переполнения |
| 3 | `Core` | [CF 687B - Remainders Game](https://codeforces.com/problemset/problem/687/B) | CF 1800 | Покрытие требуемых простых степеней через LCM |
| 4 | `Extra` | [CF 1627D - Not Adding](https://codeforces.com/problemset/problem/1627/D) | CF 1900 | Sieve-like GCD по всем кратным |

<a id="practice-extended-euclid"></a>

### 15.2. Расширенный алгоритм Евклида

Этап **A1**. Core: **1**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: extended Euclid](ROADMAP.md#topic-extended-euclid).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 7C - Line](https://codeforces.com/problemset/problem/7/C) | CF 1800 | Коэффициенты Безу и линейное диофантово уравнение |

<a id="practice-sieve-factorization"></a>

### 15.3. Решето, SPF и факторизация

Этап **A1**. Core: **5**. Extra: **3**. Теория и признаки распознавания: [ROADMAP: решето и факторизация](ROADMAP.md#topic-sieve-factorization).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 204 - Count Primes](https://leetcode.com/problems/count-primes/) | LC Medium | Решето Эратосфена |
| 2 | `Core` | [CF 1294C - Product of Three Numbers](https://codeforces.com/problemset/problem/1294/C) | CF 1300 | Пробное деление за `O(sqrt n)` |
| 3 | `Core` | [CF 546D - Soldier and Number Game](https://codeforces.com/problemset/problem/546/D) | CF 1700 | SPF-sieve и префикс числа простых множителей |
| 4 | `Core` | [CF 762A - k-th Divisor](https://codeforces.com/problemset/problem/762/A) | CF 1400 | Делители парами и возрастающий порядок |
| 5 | `Core` | [CF 1295D - Same GCDs](https://codeforces.com/problemset/problem/1295/D) | CF 1800 | Функция Эйлера после факторизации |
| 6 | `Extra` | [CF 17A - Noldbach Problem](https://codeforces.com/problemset/problem/17/A) | CF 1000 | Решето и проверка специального представления |
| 7 | `Extra` | [CF 230B - T-primes](https://codeforces.com/problemset/problem/230/B) | CF 1300 | Квадрат простого числа |
| 8 | `Extra` | [CF 26A - Almost Prime](https://codeforces.com/problemset/problem/26/A) | CF 900 | Число различных простых делителей для всех значений |

<a id="practice-congruences-crt"></a>

### 15.4. Сравнения и китайская теорема об остатках

Этап **A1/B**. Core: **2**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: сравнения и CRT](ROADMAP.md#topic-congruences-crt).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: congruence и generalized CRT | Checkpoint | Решить `a*x=b (mod m)`, проверить совместимость и объединить два сравнения |
| 2 | `Core` | [CF 1500B - Two Chandeliers](https://codeforces.com/problemset/problem/1500/B) | CF 2200 | Generalized CRT и gcd-совместимость |
| 3 | `Extra` | [CF 710D - Two Arithmetic Progressions](https://codeforces.com/problemset/problem/710/D) | CF 2500 | Пересечение арифметических прогрессий через сравнения |

<a id="practice-modular-arithmetic"></a>

## Модуль 16. Модульная арифметика и комбинаторика

### 16.1. Модульная арифметика

Этап **A1**. Core: **2**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: модульная арифметика](ROADMAP.md#topic-modular-arithmetic).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: modular API | Checkpoint | Нормализация, сложение, умножение, binpow и inverse только при выполненных условиях |
| 2 | `Core` | [CF 1514B - AND 0, Sum Big](https://codeforces.com/problemset/problem/1514/B) | CF 1200 | Быстрое возведение в степень по модулю |

<a id="practice-combinatorics"></a>

### 16.2. Сочетания и факториалы

Этап **A1**. Core: **5**. Extra: **5**. Теория и признаки распознавания: [ROADMAP: сочетания](ROADMAP.md#topic-combinatorics).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 62 - Unique Paths](https://leetcode.com/problems/unique-paths/) | LC Medium | Подсчет путей через DP или сочетание |
| 2 | `Core` | [LC 1641 - Count Sorted Vowel Strings](https://leetcode.com/problems/count-sorted-vowel-strings/) | LC Medium | Сочетания с повторениями |
| 3 | `Core` | Локальный checkpoint: factorial API | Checkpoint | `fact`, `invFact`, `C(n,k)` по простому модулю и проверка против Паскаля |
| 4 | `Core` | Локальный checkpoint: multinomial и Catalan | Checkpoint | Вывести формулы, проверить малые значения прямым DP и учесть условия модуля |
| 5 | `Core` | [CF 1444B - Divide and Sum](https://codeforces.com/problemset/problem/1444/B) | CF 1900 | Центральный биномиальный коэффициент и вклад разностей |
| 6 | `Extra` | [ACMP 158 - Великий комбинатор](https://acmp.ru/index.asp?main=task&id_task=158) | - | Размещения с повторениями |
| 7 | `Extra` | [CF 553A - Kyoya and Colored Balls](https://codeforces.com/problemset/problem/553/A) | CF 1500 | Последовательное применение сочетаний |
| 8 | `Extra` | [CF 1436C - Binary Search](https://codeforces.com/problemset/problem/1436/C) | CF 1500 | Комбинаторное моделирование пути binary search |
| 9 | `Extra` | [CF 300C - Beautiful Numbers](https://codeforces.com/problemset/problem/300/C) | CF 1800 | Перебор числа выбранных цифр и `C(n,k)` |
| 10 | `Extra` | [CF 478B - Random Teams](https://codeforces.com/problemset/problem/478/B) | CF 1300 | Экстремальное распределение и `C(x,2)` |

<a id="practice-inclusion-exclusion"></a>

### 16.3. Inclusion-exclusion

Этап **A1**. Core: **2**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: inclusion-exclusion](ROADMAP.md#topic-inclusion-exclusion).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: inclusion-exclusion | Checkpoint | Перебор маски событий, чередование знака и безопасный LCM с overflow guard |
| 2 | `Core` | [CF 340E - Iahub and Permutations](https://codeforces.com/problemset/problem/340/E) | CF 2000 | Derangements как inclusion-exclusion по фиксированным точкам |
| 3 | `Extra` | [CF 451E - Devu and Flowers](https://codeforces.com/problemset/problem/451/E) | CF 2300 | Inclusion-exclusion по верхним ограничениям |

<a id="practice-pigeonhole-counting"></a>

### 16.4. Принцип Дирихле

Этап **A1**. Core: **1**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: принцип Дирихле](ROADMAP.md#topic-pigeonhole-counting).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 1305C - Kuroni and Impossible Calculation](https://codeforces.com/problemset/problem/1305/C) | CF 1600 | Повтор остатка гарантирует нулевую разность по модулю |

<a id="practice-basic-strings"></a>

## Модуль 17. Базовые строковые алгоритмы

<a id="practice-prefix-kmp"></a>

### 17.1. Префикс-функция, KMP, границы и периоды

Этап **A1**. Core: **3**. Extra: **5**. Теория и признаки распознавания: [ROADMAP: prefix function и KMP](ROADMAP.md#topic-prefix-kmp).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Extra` | [LC 28 - Find the Index of the First Occurrence](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | LC Easy | KMP в интерфейсе поиска первого вхождения |
| 2 | `Extra` | [LC 214 - Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) | LC Hard | Палиндромный префикс через строку с разделителем |
| 3 | `Core` | Локальный checkpoint: prefix function и KMP | Checkpoint | Линейная prefix function, поиск всех вхождений и stress против прямого сравнения |
| 4 | `Core` | [ACMP 202 - Поиск подстроки](https://acmp.ru/index.asp?main=task&id_task=202) | - | KMP и все позиции начала образца |
| 5 | `Core` | [ACMP 204 - Циклическая строка](https://acmp.ru/index.asp?main=task&id_task=204) | - | Цепочка границ и минимальный период |
| 6 | `Extra` | [CF 126B - Password](https://codeforces.com/problemset/problem/126/B) | CF 1700 | Дерево границ и внутреннее вхождение |
| 7 | `Extra` | [CF 471D - MUH and Cube Walls](https://codeforces.com/problemset/problem/471/D) | CF 1800 | KMP по массиву разностей |
| 8 | `Extra` | [CF 1200E - Compress Words](https://codeforces.com/problemset/problem/1200/E) | CF 2000 | Максимальное prefix/suffix перекрытие |

<a id="practice-z-function"></a>

### 17.2. Z-функция и префиксные совпадения

Этап **A1**. Core: **3**. Extra: **18**. Теория и признаки распознавания: [ROADMAP: Z-function](ROADMAP.md#topic-z-function).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: linear Z | Checkpoint | Поддерживать правый Z-box и проверить результат против `O(n^2)` |
| 2 | `Core` | [CF EDU 3.3A - Linear Z](https://codeforces.com/edu/course/2/lesson/3/3/practice/contest/272263/problem/A) | EDU | Каноническая линейная реализация Z-function |
| 3 | `Core` | [CF EDU 3.4C - Prefix Occurrences](https://codeforces.com/edu/course/2/lesson/3/4/practice/contest/272262/problem/C) | EDU | Агрегация числа вхождений всех префиксов |
| 4 | `Extra` | [CF EDU 3.1A - Longest Palindromic Prefix-1](https://codeforces.com/edu/course/2/lesson/3/1/practice/contest/272260/problem/A) | EDU | Прямой precursor палиндромного префикса |
| 5 | `Extra` | [CF EDU 3.1B - Prefix/Suffix Substrings-1](https://codeforces.com/edu/course/2/lesson/3/1/practice/contest/272260/problem/B) | EDU | Прямой поиск границ строки |
| 6 | `Extra` | [CF EDU 3.1C - Wildcard Pattern Search](https://codeforces.com/edu/course/2/lesson/3/1/practice/contest/272260/problem/C) | EDU | Наивный поиск с wildcard перед линейной оптимизацией |
| 7 | `Extra` | [CF EDU 3.1D - Number of Good Substrings-1](https://codeforces.com/edu/course/2/lesson/3/1/practice/contest/272260/problem/D) | EDU | Наивное перечисление совпадающих подстрок |
| 8 | `Extra` | [CF EDU 3.2A - Simple Z](https://codeforces.com/edu/course/2/lesson/3/2/practice/contest/272261/problem/A) | EDU | Квадратичная Z-function как precursor |
| 9 | `Extra` | [CF EDU 3.2B - Gray-string Z](https://codeforces.com/edu/course/2/lesson/3/2/practice/contest/272261/problem/B) | EDU | Рассуждение о Z-массиве специальной строки |
| 10 | `Extra` | [CF EDU 3.2C - String from Z](https://codeforces.com/edu/course/2/lesson/3/2/practice/contest/272261/problem/C) | EDU | Восстановление строки по ограничениям Z |
| 11 | `Extra` | [CF EDU 3.4A - Minimum Period](https://codeforces.com/edu/course/2/lesson/3/4/practice/contest/272262/problem/A) | EDU | Период строки через префиксные совпадения |
| 12 | `Extra` | [CF EDU 3.4B - Cyclic Shifts](https://codeforces.com/edu/course/2/lesson/3/4/practice/contest/272262/problem/B) | EDU | Точное совпадение в циклической строке |
| 13 | `Extra` | [CF EDU 3.4D - Palindromic Prefix](https://codeforces.com/edu/course/2/lesson/3/4/practice/contest/272262/problem/D) | EDU | Z-function на строке и ее reverse |
| 14 | `Extra` | [CF EDU 3.4E - Strange Operation](https://codeforces.com/edu/course/2/lesson/3/4/practice/contest/272262/problem/E) | EDU | Прикладная интерпретация Z-значений |
| 15 | `Extra` | [CF EDU 3.4F - Shortest Superstring](https://codeforces.com/edu/course/2/lesson/3/4/practice/contest/272262/problem/F) | EDU | Prefix/suffix overlap нескольких строк |
| 16 | `Extra` | [CF EDU 3.4G - Cubes](https://codeforces.com/edu/course/2/lesson/3/4/practice/contest/272262/problem/G) | EDU | Z-function с разворотом последовательности |
| 17 | `Extra` | [CF EDU 3.4H - Sum Lengths of Distinct Substrings](https://codeforces.com/edu/course/2/lesson/3/4/practice/contest/272262/problem/H) | EDU | Повторные Z-запуски и новые подстроки |
| 18 | `Extra` | [CF EDU 3.4I - Inexact Search](https://codeforces.com/edu/course/2/lesson/3/4/practice/contest/272262/problem/I) | EDU | Forward/reverse Z для ограниченного числа несовпадений |
| 19 | `Extra` | [CF EDU 3.4J - Cyclic Suffixes](https://codeforces.com/edu/course/2/lesson/3/4/practice/contest/272262/problem/J) | EDU | Продвинутая обработка циклических совпадений |
| 20 | `Extra` | [CF 432D - Prefixes and Suffixes](https://codeforces.com/problemset/problem/432/D) | CF 2000 | Z-function и число вхождений всех границ |
| 21 | `Extra` | [CF 535D - Tavas and Malekas](https://codeforces.com/problemset/problem/535/D) | CF 1900 | Совместимость перекрывающихся шаблонов через Z |

<a id="practice-rolling-hash"></a>

### 17.3. Полиномиальный rolling hash подстрок

Этап **A1**. Core: **1**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: rolling hash](ROADMAP.md#topic-rolling-hash).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: double rolling hash | Checkpoint | Hash полуинтервала, нормализация степеней и stress против прямого сравнения |
| 2 | `Extra` | [CF 7D - Palindrome Degree](https://codeforces.com/problemset/problem/7/D) | CF 2200 | Forward/reverse hash плюс DP по палиндромным префиксам |

<a id="practice-trie"></a>

### 17.4. Trie и словарные префиксные запросы

Этап **A1**. Core: **2**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: trie](ROADMAP.md#topic-trie).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 208 - Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) | LC Medium | `insert/search/startsWith` и terminal flag |
| 2 | `Core` | Локальный checkpoint: trie на primitive arrays | Checkpoint | `next`, `terminal`, `prefixCount`, удаление счетчиками и оценка памяти |
| 3 | `Extra` | [CF 514C - Watto and Mechanism](https://codeforces.com/problemset/problem/514/C) | CF 1700 | Trie или hash и ровно одно несовпадение |
| 4 | `Extra` | [CF 271D - Good Substrings](https://codeforces.com/problemset/problem/271/D) | CF 1800 | Trie различных подстрок с лимитом плохих символов |

<a id="practice-graph-representation"></a>

## Модуль 18. Связность графов

### 18.1. Модель графа и представление в памяти

Этап **A1**. Core: **2**. Extra: **18**. Теория и признаки распознавания: [ROADMAP: модель графа](ROADMAP.md#topic-graph-representation).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF EDU 8.4A - Adjacency Matrix](https://codeforces.com/edu/course/2/lesson/8/4/practice/contest/290943/problem/A) | EDU | Построение матрицы смежности |
| 2 | `Core` | [CF EDU 8.4C - Adjacency Lists](https://codeforces.com/edu/course/2/lesson/8/4/practice/contest/290943/problem/C) | EDU | Построение списков смежности |
| 3 | `Extra` | [CF EDU 8.1A - Undirected Graph?](https://codeforces.com/edu/course/2/lesson/8/1/practice/contest/290939/problem/A) | EDU | Проверка свойств неориентированного графа |
| 4 | `Extra` | [CF EDU 8.1B - Degrees](https://codeforces.com/edu/course/2/lesson/8/1/practice/contest/290939/problem/B) | EDU | Подсчет степеней вершин |
| 5 | `Extra` | [CF EDU 8.1C - Sequence Type](https://codeforces.com/edu/course/2/lesson/8/1/practice/contest/290939/problem/C) | EDU | Различение walk, path и cycle |
| 6 | `Extra` | [CF EDU 8.1D - Components?](https://codeforces.com/edu/course/2/lesson/8/1/practice/contest/290939/problem/D) | EDU | Рассуждение о компонентах |
| 7 | `Extra` | [CF EDU 8.1E - Tree Degrees](https://codeforces.com/edu/course/2/lesson/8/1/practice/contest/290939/problem/E) | EDU | Инвариант суммы степеней дерева |
| 8 | `Extra` | [CF EDU 8.1F - Graph from Degree Array](https://codeforces.com/edu/course/2/lesson/8/1/practice/contest/290939/problem/F) | EDU | Конструкция по последовательности степеней |
| 9 | `Extra` | [CF EDU 8.1G - Graph from Degree Set](https://codeforces.com/edu/course/2/lesson/8/1/practice/contest/290939/problem/G) | EDU | Конструкция по множеству степеней |
| 10 | `Extra` | [CF EDU 8.2A - Number of Vertices](https://codeforces.com/edu/course/2/lesson/8/2/practice/contest/290940/problem/A) | EDU | Формулы для числа вершин и ребер |
| 11 | `Extra` | [CF EDU 8.2B - Regular Graph](https://codeforces.com/edu/course/2/lesson/8/2/practice/contest/290940/problem/B) | EDU | Свойства регулярного графа |
| 12 | `Extra` | [CF EDU 8.2C - Empty and Complete](https://codeforces.com/edu/course/2/lesson/8/2/practice/contest/290940/problem/C) | EDU | Пустой и полный граф |
| 13 | `Extra` | [CF EDU 8.2D - Complete Components](https://codeforces.com/edu/course/2/lesson/8/2/practice/contest/290940/problem/D) | EDU | Компонента как clique |
| 14 | `Extra` | [CF EDU 8.3A - Sources/Sinks](https://codeforces.com/edu/course/2/lesson/8/3/practice/contest/290941/problem/A) | EDU | Входящие и исходящие степени |
| 15 | `Extra` | [CF EDU 8.3B - Functional Graph](https://codeforces.com/edu/course/2/lesson/8/3/practice/contest/290941/problem/B) | EDU | Модель функционального графа |
| 16 | `Extra` | [CF EDU 8.3C - Equal Degrees](https://codeforces.com/edu/course/2/lesson/8/3/practice/contest/290941/problem/C) | EDU | Конструкция ориентированного графа |
| 17 | `Extra` | [CF EDU 8.3D - Second Neighbors](https://codeforces.com/edu/course/2/lesson/8/3/practice/contest/290941/problem/D) | EDU | Двухшаговая смежность |
| 18 | `Extra` | [CF EDU 8.4B - Validate Matrix](https://codeforces.com/edu/course/2/lesson/8/4/practice/contest/290943/problem/B) | EDU | Инварианты матрицы неориентированного графа |
| 19 | `Extra` | [CF EDU 8.4D - Two Edges](https://codeforces.com/edu/course/2/lesson/8/4/practice/contest/290943/problem/D) | EDU | Подсчет путей длины два |
| 20 | `Extra` | [CF EDU 8.4E - Complete Subgraphs](https://codeforces.com/edu/course/2/lesson/8/4/practice/contest/290943/problem/E) | EDU | Компоненты и проверка clique |

<a id="practice-graph-traversals"></a>

### 18.2. DFS/BFS: достижимость, компоненты и flood fill

Этап **A1**. Core: **1**. Extra: **5**. Теория и признаки распознавания: [ROADMAP: обходы графа](ROADMAP.md#topic-graph-traversals).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 200 - Number of Islands](https://leetcode.com/problems/number-of-islands/) | LC Medium | Flood fill и число компонент |
| 2 | `Extra` | [CF 1829E - The Lakes](https://codeforces.com/problemset/problem/1829/E) | CF 1100 | Компонента с агрегированием веса |
| 3 | `Extra` | [CF 217A - Ice Skating](https://codeforces.com/problemset/problem/217/A) | CF 1200 | Компоненты неявно заданного графа |
| 4 | `Extra` | [CF 500A - New Year Transportation](https://codeforces.com/problemset/problem/500/A) | CF 1000 | Достижимость в функциональном графе |
| 5 | `Extra` | [CF 377A - Maze](https://codeforces.com/problemset/problem/377/A) | CF 1600 | Сохранение связного подмножества клеток |
| 6 | `Extra` | [CF 1365D - Solve The Maze](https://codeforces.com/problemset/problem/1365/D) | CF 1700 | Локальное блокирование клеток и затем глобальная проверка DFS |

<a id="practice-graph-cycles"></a>

### 18.3. Циклы в ориентированном и неориентированном графе

Этап **A1**. Core: **1**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: циклы](ROADMAP.md#topic-graph-cycles).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 510B - Fox And Two Dots](https://codeforces.com/problemset/problem/510/B) | CF 1500 | Цикл в неориентированной сетке с parent |

<a id="practice-bipartite"></a>

### 18.4. Двудольность и раскраска в два цвета

Этап **A1**. Core: **1**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: двудольность](ROADMAP.md#topic-bipartite).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 785 - Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) | LC Medium | Раскраска каждой компоненты в два цвета |
| 2 | `Extra` | [CF 687A - NP-Hard Problem](https://codeforces.com/problemset/problem/687/A) | CF 1500 | Вывод двух долей общего графа |
| 3 | `Extra` | [CF 1702E - Split Into Two Sets](https://codeforces.com/problemset/problem/1702/E) | CF 1600 | Степени плюс двудольность графа из пар |

<a id="practice-dsu"></a>

### 18.5. DSU: объединение компонент и метаданные корня

Этап **A1/B**. Core: **6**. Extra: **8**. Теория и признаки распознавания: [ROADMAP: DSU](ROADMAP.md#topic-dsu).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Extra` | [LC 721 - Accounts Merge](https://leetcode.com/problems/accounts-merge/) | LC Medium | Объединение по общим строковым идентификаторам |
| 2 | `Core` | Локальный checkpoint: DSU API | Checkpoint | `find/union/same/componentSize/components` и stress против явных компонент |
| 3 | `Core` | [CF EDU 7.1A - Basic DSU](https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/A) | EDU | Path compression и union by size |
| 4 | `Core` | [CF EDU 7.1B - DSU 2](https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B) | EDU | Min, max и size как метаданные корня |
| 5 | `Core` | [CF 1167C - News Distribution](https://codeforces.com/problemset/problem/1167/C) | CF 1400 | Групповые объединения и размер компоненты |
| 6 | `Core` | [CF 25D - Roads not only in Berland](https://codeforces.com/problemset/problem/25/D) | CF 1700 | Лишние ребра и восстановление связного дерева |
| 7 | `Core` | [CSES - Road Construction](https://cses.fi/problemset/task/1676) | - | Online union, число компонент и максимум размера |
| 8 | `Extra` | [CF 1012B - Chemical Table](https://codeforces.com/problemset/problem/1012/B) | CF 1800 | Двудольная модель компонент строк и столбцов |
| 9 | `Extra` | [CF EDU 7.1C - Experience](https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C) | EDU | Weighted DSU с потенциалом к корню |
| 10 | `Extra` | [CF EDU 7.1D - Cutting Graph](https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D) | EDU | Offline reverse deletions |
| 11 | `Extra` | [CF EDU 7.1E - Monkeys](https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/E) | EDU | Reverse activation и время присоединения |
| 12 | `Extra` | [CF EDU 7.2D - Bosses](https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/D) | EDU | Weighted successor relation |
| 13 | `Extra` | [CF EDU 7.2I - Bipartite Graph](https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/I) | EDU | Parity DSU |
| 14 | `Extra` | [CF EDU 7.2J - First Non-bipartite Edge](https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/J) | EDU | Parity conflict и первый нарушающий запрос |

<a id="practice-dsu-next"></a>

### 18.6. Successor DSU и пропуск обработанных позиций

Этап **A1**. Core: **3**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: successor DSU](ROADMAP.md#topic-dsu-next).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF EDU 7.2A - People Leave](https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A) | EDU | Следующий еще активный индекс |
| 2 | `Core` | [CF EDU 7.2B - Parking](https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/B) | EDU | Циклический successor с переходом через начало |
| 3 | `Core` | [CF EDU 7.2C - Company Restructuring](https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/C) | EDU | Пропуск уже объединенных границ диапазона |

<a id="practice-shortest-paths"></a>

## Модуль 19. Кратчайшие пути

<a id="practice-bfs-shortest"></a>

### 19.1. BFS shortest path и multi-source BFS

Этап **A1**. Core: **1**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: BFS shortest path](ROADMAP.md#topic-bfs-shortest).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 520B - Two Buttons](https://codeforces.com/problemset/problem/520/B) | CF 1400 | BFS по неявному невзвешенному графу состояний |
| 2 | `Extra` | [ACMP 99 - Лабиринт](https://acmp.ru/index.asp?main=task&id_task=99) | - | BFS в трехмерной сетке |

<a id="practice-zero-one-bfs"></a>

### 19.2. 0-1 BFS

Этап **A1**. Core: **1**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: 0-1 BFS](ROADMAP.md#topic-zero-one-bfs).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 1063B - Labyrinth](https://codeforces.com/problemset/problem/1063/B) | CF 1800 | Ребра веса 0/1 и deque вместо heap |

<a id="practice-dijkstra"></a>

### 19.3. Dijkstra для неотрицательных весов

Этап **A1**. Core: **2**. Extra: **3**. Теория и признаки распознавания: [ROADMAP: Dijkstra](ROADMAP.md#topic-dijkstra).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 743 - Network Delay Time](https://leetcode.com/problems/network-delay-time/) | LC Medium | Dijkstra по списку ребер |
| 2 | `Core` | [CF 20C - Dijkstra?](https://codeforces.com/problemset/problem/20/C) | CF 1900 | Lazy heap, `parent[]` и восстановление пути |
| 3 | `Extra` | [ACMP 132 - Алгоритм Дейкстры](https://acmp.ru/index.asp?main=task&id_task=132) | - | Базовые релаксации Dijkstra |
| 4 | `Extra` | [CF 938D - Buy a Ticket](https://codeforces.com/problemset/problem/938/D) | CF 2000 | Multi-source Dijkstra с разными стартовыми расстояниями |
| 5 | `Extra` | [CF 449B - Jzzhu and Cities](https://codeforces.com/problemset/problem/449/B) | CF 2000 | Несколько типов стартовых ребер и подсчет избыточных |

<a id="practice-bellman-ford"></a>

### 19.4. Bellman-Ford, ограничение числа ребер и отрицательный цикл

Этап **A1**. Core: **1**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: Bellman-Ford](ROADMAP.md#topic-bellman-ford).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Extra` | [LC 787 - Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | LC Medium | Layered Bellman-Ford с лимитом числа ребер |
| 2 | `Core` | [ACMP 138 - Алгоритм Форда-Беллмана](https://acmp.ru/index.asp?main=task&id_task=138) | - | `n-1` раундов релаксации ребер |
| 3 | `Extra` | [ACMP 140 - Цикл отрицательного веса](https://acmp.ru/index.asp?main=task&id_task=140) | - | Обнаружение и восстановление отрицательного цикла |

<a id="practice-floyd-warshall"></a>

### 19.5. Floyd-Warshall и все пары кратчайших путей

Этап **A1**. Core: **1**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: Floyd-Warshall](ROADMAP.md#topic-floyd-warshall).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [ACMP 135 - Алгоритм Флойда](https://acmp.ru/index.asp?main=task&id_task=135) | - | Разрешать промежуточные вершины по одной |
| 2 | `Extra` | [CF 295B - Greg and Graph](https://codeforces.com/problemset/problem/295/B) | CF 1700 | Обратное добавление вершин во Floyd |

<a id="practice-trees-lca"></a>

## Модуль 20. Базовые алгоритмы на деревьях

<a id="practice-rooted-trees"></a>

### 20.1. Корневое дерево, parent/depth, поддерево и диаметр

Этап **A1**. Core: **2**. Extra: **5**. Теория и признаки распознавания: [ROADMAP: корневое дерево](ROADMAP.md#topic-rooted-trees).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Extra` | [LC 863 - All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | LC Medium | Добавить parent и обходить дерево как граф |
| 2 | `Core` | [CF 115A - Party](https://codeforces.com/problemset/problem/115/A) | CF 900 | Parent, depth и высота леса |
| 3 | `Core` | Локальный checkpoint: базовое дерево | Checkpoint | Parent/depth/subtree size, диаметр и восстановление пути |
| 4 | `Extra` | [ACMP 141 - Дерево](https://acmp.ru/index.asp?main=task&id_task=141) | - | Проверка связности и числа ребер |
| 5 | `Extra` | [CF 1057A - Bmail Computer Network](https://codeforces.com/problemset/problem/1057/A) | CF 900 | Восстановление пути по parent |
| 6 | `Extra` | [CF 580C - Kefa and Park](https://codeforces.com/problemset/problem/580/C) | CF 1500 | Состояние на пути корневого DFS |
| 7 | `Extra` | [CF 1676G - White-Black Balanced Subtrees](https://codeforces.com/problemset/problem/1676/G) | CF 1300 | Postorder-агрегация поддерева |

<a id="practice-euler-tour"></a>

### 20.2. Euler tin/tout и поддерево как отрезок

Этап **A1**. Core: **2**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: Euler tour](ROADMAP.md#topic-euler-tour).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 1006E - Military Problem](https://codeforces.com/problemset/problem/1006/E) | CF 1600 | Preorder flatten и размер поддерева |
| 2 | `Core` | [CF 1328E - Tree Queries](https://codeforces.com/problemset/problem/1328/E) | CF 1900 | Ancestor relation через `tin/tout` |
| 3 | `Extra` | [CF 383C - Propagating Tree](https://codeforces.com/problemset/problem/383/C) | CF 2000 | Euler flatten плюс Fenwick с четностью глубины |
| 4 | `Extra` | [CF 570D - Tree Requests](https://codeforces.com/problemset/problem/570/D) | CF 2000 | Euler interval и offline buckets по глубине |

<a id="practice-lca"></a>

### 20.3. Binary lifting, k-й предок, LCA и расстояние

Этап **A1**. Core: **2**. Extra: **4**. Теория и признаки распознавания: [ROADMAP: binary lifting и LCA](ROADMAP.md#topic-lca).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Extra` | [LC 236 - Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | LC Medium | Рекурсивный LCA без preprocessing |
| 2 | `Core` | [CSES - Company Queries I](https://cses.fi/problemset/task/1687) | - | K-й предок двоичными подъемами |
| 3 | `Core` | [CSES - Company Queries II](https://cses.fi/problemset/task/1688) | - | LCA двух вершин |
| 4 | `Extra` | [CF 1304E - 1-Trees and Queries](https://codeforces.com/problemset/problem/1304/E) | CF 2000 | LCA, расстояния и четность маршрута |
| 5 | `Extra` | [CF Gym 100091B - LCA Продолжение](https://codeforces.com/gym/100091/problem/B) | - | Online binary lifting при добавлении листьев |
| 6 | `Extra` | [CF 519E - A and B and Lecture Rooms](https://codeforces.com/problemset/problem/519/E) | CF 2100 | Подъемы и размеры частей дерева |

<a id="practice-tree-differences"></a>

### 20.4. Difference-on-tree для массовых добавлений

Этап **B**. Core: **1**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: difference-on-tree](ROADMAP.md#topic-tree-differences).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 191C - Fools and Roads](https://codeforces.com/problemset/problem/191/C) | CF 1900 | Разности в концах пути, поправка в LCA и postorder |

<a id="practice-basic-dp-state"></a>

## Модуль 21. Базовое DP и DAG

### 21.1. Проектирование DP-состояния

Этап **A1**. Core: **3**. Extra: **9**. Теория и признаки распознавания: [ROADMAP: проектирование DP-состояния](ROADMAP.md#topic-basic-dp-state).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [ACMP 11 - Зайчик](https://acmp.ru/index.asp?main=task&id_task=11) | - | Одномерная рекуррентность и число способов |
| 2 | `Core` | [CF 698A - Vacations](https://codeforces.com/problemset/problem/698/A) | CF 1400 | Малое состояние предыдущего действия |
| 3 | `Core` | [CF 706C - Hard Problem](https://codeforces.com/problemset/problem/706/C) | CF 1600 | Два состояния строки, `INF` и переходы |
| 4 | `Extra` | [CF 1950D - Product of Binary Decimals](https://codeforces.com/problemset/problem/1950/D) | CF 1100 | Memoization по повторяющимся значениям |
| 5 | `Extra` | [ACMP 121 - Гвоздики](https://acmp.ru/index.asp?main=task&id_task=121) | - | Линейное DP после сортировки |
| 6 | `Extra` | [CF 455A - Boredom](https://codeforces.com/problemset/problem/455/A) | CF 1500 | Choose/skip DP по сжатым частотам |
| 7 | `Extra` | [CF 474D - Flowers](https://codeforces.com/problemset/problem/474/D) | CF 1700 | Число способов переходами двух размеров |
| 8 | `Extra` | [CF 327A - Flipping Game](https://codeforces.com/problemset/problem/327/A) | CF 1200 | Максимальный подотрезок после преобразования выигрыша |
| 9 | `Extra` | [CF 1195C - Basketball Exercise](https://codeforces.com/problemset/problem/1195/C) | CF 1400 | Prefix DP с двумя рядами |
| 10 | `Extra` | [CF 118D - Caesar's Legions](https://codeforces.com/problemset/problem/118/D) | CF 1700 | Состояние по длине, последнему типу и длине серии |
| 11 | `Extra` | [CF 225C - Barcode](https://codeforces.com/problemset/problem/225/C) | CF 1700 | DP по префиксу и длине одноцветного блока |
| 12 | `Extra` | [CSES - Word Combinations](https://cses.fi/problemset/task/1731) | - | DP по позиции плюс trie словаря |

<a id="practice-knapsack"></a>

### 21.2. Knapsack и subset-sum

Этап **A1**. Core: **2**. Extra: **3**. Теория и признаки распознавания: [ROADMAP: knapsack](ROADMAP.md#topic-knapsack).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 322 - Coin Change](https://leetcode.com/problems/coin-change/) | LC Medium | Unbounded knapsack и порядок циклов |
| 2 | `Core` | [CSES - Book Shop](https://cses.fi/problemset/task/1158) | - | 0/1 knapsack одним массивом справа налево |
| 3 | `Extra` | [CF 189A - Cut Ribbon](https://codeforces.com/problemset/problem/189/A) | CF 1300 | Unbounded knapsack на максимум числа предметов |
| 4 | `Extra` | [CF 577B - Modulo Sum](https://codeforces.com/problemset/problem/577/B) | CF 1900 | 0/1 subset-sum по остаткам плюс pigeonhole |
| 5 | `Extra` | [CF 864E - Fire](https://codeforces.com/problemset/problem/864/E) | CF 2000 | Knapsack с дедлайнами и восстановлением набора |

<a id="practice-sequence-dp"></a>

### 21.3. DP двух последовательностей: LCS и edit distance

Этап **A1**. Core: **1**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: sequence DP](ROADMAP.md#topic-sequence-dp).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CSES - Edit Distance](https://cses.fi/problemset/task/1639) | - | Таблица по двум префиксам и три типа перехода |

<a id="practice-lis"></a>

### 21.4. LIS и DP по подпоследовательности

Этап **A1**. Core: **1**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: LIS](ROADMAP.md#topic-lis).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 300 - Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | LC Medium | `tails` и lower bound |
| 2 | `Extra` | [CF 4D - Mysterious Present](https://codeforces.com/problemset/problem/4/D) | CF 1700 | LIS-подобное DP с parent |
| 3 | `Extra` | [CF 977F - Consecutive Subsequence](https://codeforces.com/problemset/problem/977/F) | CF 1700 | DP по значению и восстановление индексов |

<a id="practice-topological-sort"></a>

### 21.5. Topological sort и цикл в ориентированном графе

Этап **A1**. Core: **2**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: topological sort](ROADMAP.md#topic-topological-sort).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CSES - Course Schedule](https://cses.fi/problemset/task/1679) | - | Kahn, indegree и обнаружение цикла |
| 2 | `Core` | [CF 510C - Fox And Names](https://codeforces.com/problemset/problem/510/C) | CF 1700 | Построение ограничений порядка символов |
| 3 | `Extra` | [CF 1385E - Directing Edges](https://codeforces.com/problemset/problem/1385/E) | CF 1900 | Ориентация свободных ребер по topological order |

<a id="practice-dag-dp"></a>

### 21.6. DP и релаксации по DAG

Этап **A1**. Core: **3**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: DAG DP](ROADMAP.md#topic-dag-dp).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CSES - Longest Flight Route](https://cses.fi/problemset/task/1680) | - | Максимальный путь и восстановление parent |
| 2 | `Core` | [CF 919D - Substring](https://codeforces.com/problemset/problem/919/D) | CF 1800 | Векторное DP по topological order |
| 3 | `Core` | [CSES - Game Routes](https://cses.fi/problemset/task/1681) | - | Число путей по модулю |
| 4 | `Extra` | [CF 721C - Journey](https://codeforces.com/problemset/problem/721/C) | CF 2200 | DP по времени и числу вершин с восстановлением |

<a id="practice-fenwick"></a>

## Модуль 22. Fenwick tree

<a id="practice-fenwick-basic"></a>

### 22.1. Изменяемые префиксные суммы

Этап **A1**. Core: **1**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: базовый Fenwick](ROADMAP.md#topic-fenwick-basic).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Extra` | [LC 307 - Range Sum Query Mutable](https://leetcode.com/problems/range-sum-query-mutable/) | LC Medium | Point assignment через delta и range sum |
| 2 | `Core` | [ACMP 1084 - Дерево Фенвика](https://acmp.ru/index.asp?main=task&id_task=1084) | - | `add`, prefix sum и range sum |
| 3 | `Extra` | [CF EDU 4.3E - Range Add](https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/E) | EDU | Difference Fenwick для range add и point query |

<a id="practice-fenwick-offline"></a>

### 22.2. Offline counting и dominance

Этап **A1**. Core: **2**. Extra: **5**. Теория и признаки распознавания: [ROADMAP: offline Fenwick](ROADMAP.md#topic-fenwick-offline).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF EDU 4.3A - Inversions](https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/A) | EDU | Fenwick частот уже просмотренных рангов |
| 2 | `Core` | [CF 652D - Nested Segments](https://codeforces.com/problemset/problem/652/D) | CF 1800 | Сортировка по одной границе и dominance по другой |
| 3 | `Extra` | [CF 459D - Pashmak and Parmida's Problem](https://codeforces.com/problemset/problem/459/D) | CF 1800 | Частотные ранги и подсчет пар |
| 4 | `Extra` | [CF 61E - Enemy Is Weak](https://codeforces.com/problemset/problem/61/E) | CF 1900 | Вклад среднего элемента в убывающие тройки |
| 5 | `Extra` | [CF 220B - Little Elephant and Array](https://codeforces.com/problemset/problem/220/B) | CF 2200 | События по правой границе запроса |
| 6 | `Extra` | [CF EDU 4.3C - Nested Segments](https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/C) | EDU | Offline counting вложенных пар концов |
| 7 | `Extra` | [CF EDU 4.3D - Intersecting Segments](https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/D) | EDU | Два прохода для пересекающихся пар отрезков |

<a id="practice-fenwick-order-statistics"></a>

### 22.3. Prefix lower bound и порядковые статистики

Этап **A1**. Core: **1**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: Fenwick lower bound](ROADMAP.md#topic-fenwick-order-statistics).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 1208D - Restore Permutation](https://codeforces.com/problemset/problem/1208/D) | CF 1900 | Binary lifting по Fenwick для взвешенного prefix lower bound |
| 2 | `Extra` | [CF EDU 4.3B - Inversions 2](https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/B) | EDU | Восстановление по порядковой статистике |

<a id="practice-static-rmq"></a>

## Модуль 23. Static RMQ и sparse table

Этап **A1**. Core: **3**. Extra: **3**. Теория и признаки распознавания: [ROADMAP: static RMQ](ROADMAP.md#topic-static-rmq).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: sparse table | Checkpoint | RMQ min и stress всех непустых диапазонов против прямого ответа |
| 2 | `Core` | [CSES - Static Range Minimum Queries](https://cses.fi/problemset/task/1647) | - | Два перекрывающихся блока для idempotent min |
| 3 | `Core` | [CF 1548B - Integers Have Friends](https://codeforces.com/problemset/problem/1548/B) | CF 1800 | GCD table на разностях и монотонная граница |
| 4 | `Extra` | [CF 1709D - Rorororobot](https://codeforces.com/problemset/problem/1709/D) | CF 1700 | Static range maximum плюс арифметическая достижимость |
| 5 | `Extra` | [CF 359D - Pair of Numbers](https://codeforces.com/problemset/problem/359/D) | CF 2000 | Min/GCD tables, поиск длины и восстановление ответов |
| 6 | `Extra` | [CF 474F - Ant Colony](https://codeforces.com/problemset/problem/474/F) | CF 2100 | GCD диапазона плюс частота точного значения |

<a id="practice-segment-tree"></a>

## Модуль 24. Segment tree

<a id="practice-segment-tree-monoid"></a>

### 24.1. Point update, range aggregate и custom node

Этап **A1/B**. Core: **5**. Extra: **5**. Теория и признаки распознавания: [ROADMAP: segment tree monoid](ROADMAP.md#topic-segment-tree-monoid).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF EDU 4.1A - Sum](https://codeforces.com/edu/course/2/lesson/4/1/practice/contest/273169/problem/A) | EDU | Базовый point update и range sum |
| 2 | `Core` | [CF 380C - Sereja and Brackets](https://codeforces.com/problemset/problem/380/C) | CF 2000 | Ассоциативный custom node для скобок |
| 3 | `Core` | [CF EDU 4.2A - Maximum Subarray Sum](https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/A) | EDU | Узел `sum/pref/suf/best` |
| 4 | `Core` | [CF EDU 4.4B - Cryptography](https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/B) | EDU | Некоммутативное произведение матриц |
| 5 | `Core` | [CF EDU 4.4C - Inversions on Segment](https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/C) | EDU | Rich node с гистограммой значений |
| 6 | `Extra` | [CF 339D - Xenia and Bit Operations](https://codeforces.com/problemset/problem/339/D) | CF 1700 | Merge, зависящий от уровня дерева |
| 7 | `Extra` | [CF EDU 4.1B - Minimum](https://codeforces.com/edu/course/2/lesson/4/1/practice/contest/273169/problem/B) | EDU | Замена sum monoid на min |
| 8 | `Extra` | [CF EDU 4.1C - Number of Minimums](https://codeforces.com/edu/course/2/lesson/4/1/practice/contest/273169/problem/C) | EDU | Узел `(minimum,count)` |
| 9 | `Extra` | [CF EDU 4.4A - Alternating Sum](https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/A) | EDU | Знаковое преобразование обычной суммы |
| 10 | `Extra` | [CF EDU 4.4D - Distinct on Segment](https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/D) | EDU | Bitmask OR как агрегат |

<a id="practice-segment-tree-descent"></a>

### 24.2. Спуск по агрегату и поиск позиции

Этап **A1/B**. Core: **2**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: descent](ROADMAP.md#topic-segment-tree-descent).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF EDU 4.2B - K-th One](https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/B) | EDU | Выбор дочерней вершины по числу единиц |
| 2 | `Core` | [CF EDU 4.2D - First Element At Least X 2](https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/D) | EDU | Первый подходящий индекс не раньше `l` |
| 3 | `Extra` | [CF EDU 4.2C - First Element At Least X](https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/C) | EDU | Первый индекс с достаточным максимумом |
| 4 | `Extra` | [CF 19D - Points](https://codeforces.com/problemset/problem/19/D) | CF 2800 | Dynamic 2D dominance и descent по максимуму `y` |

<a id="practice-range-update-point-query"></a>

### 24.3. Range update и point query

Этап **A1/B**. Core: **2**. Extra: **3**. Теория и признаки распознавания: [ROADMAP: range update/point query](ROADMAP.md#topic-range-update-point-query).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF EDU 5.1C - Assignment to Segment](https://codeforces.com/edu/course/2/lesson/5/1/practice/contest/279634/problem/C) | EDU | Overwrite tag без агрегата детей |
| 2 | `Core` | [CF EDU 5.4E - Wall](https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/E) | EDU | Композиция clamp-функций и итоговый point output |
| 3 | `Extra` | [CF EDU 5.1A - Addition to Segment](https://codeforces.com/edu/course/2/lesson/5/1/practice/contest/279634/problem/A) | EDU | Add tag и point query |
| 4 | `Extra` | [CF EDU 5.1B - Maximal Segment](https://codeforces.com/edu/course/2/lesson/5/1/practice/contest/279634/problem/B) | EDU | Range chmax и point query |
| 5 | `Extra` | [CF EDU 5.4B - Addition of Arithmetic Progression](https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/B) | EDU | Coordinate-dependent lazy tag |

<a id="practice-lazy-segment-tree"></a>

### 24.4. Полный lazy propagation

Этап **A1/B**. Core: **10**. Extra: **5**. Теория и признаки распознавания: [ROADMAP: lazy propagation](ROADMAP.md#topic-lazy-segment-tree).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF EDU 5.2A - Addition and Minimum](https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/A) | EDU | Range add и range min |
| 2 | `Core` | [CF EDU 5.2C - Bitwise OR and AND](https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/C) | EDU | Нетривиальное действие OR-tag на AND-агрегат |
| 3 | `Core` | [CF EDU 5.2E - Assignment and Minimum](https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/E) | EDU | Overwrite tag и явный `hasAssign` |
| 4 | `Core` | [CF EDU 5.3A - Assignment and Maximum Subarray](https://codeforces.com/edu/course/2/lesson/5/3/practice/contest/280799/problem/A) | EDU | Lazy assignment над custom node |
| 5 | `Core` | [CF EDU 5.3B - Inverse and K-th One](https://codeforces.com/edu/course/2/lesson/5/3/practice/contest/280799/problem/B) | EDU | Flip tag плюс descent |
| 6 | `Core` | [CF EDU 5.3C - Addition and First Element At Least X](https://codeforces.com/edu/course/2/lesson/5/3/practice/contest/280799/problem/C) | EDU | Add tag плюс поиск позиции |
| 7 | `Core` | [CF EDU 5.4A - Assignment, Addition, and Sum](https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/A) | EDU | Композиция assign и add |
| 8 | `Core` | [CF EDU 5.4C - Painter](https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/C) | EDU | Assign, граничные цвета и число компонент |
| 9 | `Core` | [CF EDU 5.4D - Weighted Sum](https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/D) | EDU | Взвешенный агрегат и действие тега |
| 10 | `Core` | [CF EDU 5.4F - Hills](https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/F) | EDU | Lazy assignment плюс prefix search |
| 11 | `Extra` | [CF EDU 5.2B - Multiplication and Sum](https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/B) | EDU | Один multiplicative tag по модулю |
| 12 | `Extra` | [CF EDU 5.2D - Addition and Sum](https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/D) | EDU | Add tag и sum с учетом длины |
| 13 | `Extra` | [CF EDU 5.2F - Assignment and Sum](https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/F) | EDU | Assign tag и sum |
| 14 | `Extra` | [CF 52C - Circular RMQ](https://codeforces.com/problemset/problem/52/C) | CF 2200 | Add/min и обертка циклического диапазона |
| 15 | `Extra` | [CF 242E - XOR on Segment](https://codeforces.com/problemset/problem/242/E) | CF 2000 | Bit counts и range XOR tag |

<a id="practice-segment-tree-pruning"></a>

### 24.5. Амортизированное pruning

Этап **C**. Core: **2**. Extra: **0**. Теория и признаки распознавания: [ROADMAP: segment tree pruning](ROADMAP.md#topic-segment-tree-pruning).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF EDU 4.4E - Earthquakes](https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/E) | EDU | Останавливать рекурсию по экстремуму узла |
| 2 | `Core` | [CF 438D - The Child and Sequence](https://codeforces.com/problemset/problem/438/D) | CF 2300 | Modulo update и pruning по максимуму |

<a id="practice-geometry"></a>

## Модуль 25. Вычислительная геометрия

<a id="practice-geometry-predicates"></a>

### 25.1. Точные геометрические предикаты и пересечения

Этап **B**. Core: **4**. Extra: **3**. Теория: [ROADMAP](ROADMAP.md#topic-geometry-predicates).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Extra` | [LC 149 - Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/) | LC Hard | Нормализация направления через gcd и группы коллинеарных точек |
| 2 | `Core` | [CSES - Point Location Test](https://cses.fi/problemset/task/2189) | - | Знак cross product и left/right/touch |
| 3 | `Core` | [ACMP 348 - Пересечение отрезков](https://acmp.ru/index.asp?main=task&id_task=348) | - | Orientation, point-on-segment и вырожденные пересечения |
| 4 | `Core` | [CF 772B - Volatile Kite](https://codeforces.com/problemset/problem/772/B) | CF 1800 | Расстояние от точки до прямой через cross product |
| 5 | `Core` | Локальный checkpoint: Geometry primitives | Checkpoint | Dot/cross, projection, distance to segment и stress пересечений на целых координатах |
| 6 | `Extra` | [CF 13B - Letter A](https://codeforces.com/problemset/problem/13/B) | CF 1900 | Пересечения и геометрические ограничения составной фигуры |
| 7 | `Extra` | [CSES - Line Segment Intersection](https://cses.fi/problemset/task/2190) | - | Повтор точных предикатов на вырожденных случаях |

<a id="practice-polygons"></a>

### 25.2. Простые многоугольники: площадь и point-in-polygon

Этап **B**. Core: **3**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-polygons).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [ACMP 370 - Площадь многоугольника](https://acmp.ru/index.asp?main=task&id_task=370) | - | Shoelace и удвоенная ориентированная площадь |
| 2 | `Core` | [CSES - Point in Polygon](https://cses.fi/problemset/task/2192) | - | Boundary check плюс ray casting с корректными вершинами |
| 3 | `Core` | Локальный checkpoint: polygon API | Checkpoint | Area, boundary, inside/outside на выпуклых и невыпуклых многоугольниках |
| 4 | `Extra` | [CF 993A - Two Squares](https://codeforces.com/problemset/problem/993/A) | CF 1600 | Пересечения сторон и containment выпуклых фигур |

<a id="practice-convex-hull"></a>

### 25.3. Выпуклая оболочка и запросы на ней

Этап **B**. Core: **3**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-convex-hull).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [ACMP 374 - Выпуклая оболочка - 2](https://acmp.ru/index.asp?main=task&id_task=374) | - | Monotone chain и политика коллинеарных точек |
| 2 | `Core` | [CSES - Convex Hull](https://cses.fi/problemset/task/2195) | - | Полная `O(n log n)` оболочка с граничными точками |
| 3 | `Core` | [CF 166B - Polygons](https://codeforces.com/problemset/problem/166/B) | CF 2100 | Строгий point-in-convex за `O(log n)` без касаний |
| 4 | `Extra` | [CF 70D - Professor's task](https://codeforces.com/problemset/problem/70/D) | CF 2600 | Динамическая выпуклая оболочка и point location |

<a id="practice-rotating-calipers"></a>

### 25.4. Вращающиеся калиперы

Этап **C**. Core: **2**. Extra: **0**. Теория: [ROADMAP](ROADMAP.md#topic-rotating-calipers).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: diameter of convex polygon | Checkpoint | Оболочка уже дана; два циклических указателя и сравнение squared distance |
| 2 | `Core` | [CF Gym 101554D - Robert Hood](https://codeforces.com/gym/101554/problem/D) | - | Convex hull плюс rotating calipers для диаметра множества |

<a id="practice-geometry-sweep"></a>

### 25.5. Геометрический sweep

Этап **C**. Core: **3**. Extra: **0**. Теория: [ROADMAP](ROADMAP.md#topic-geometry-sweep).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CSES - Intersection Points](https://cses.fi/problemset/task/1740) | - | Sweep горизонтальных/вертикальных отрезков плюс Fenwick |
| 2 | `Core` | Локальный checkpoint: segment events | Checkpoint | Start/query/end tie-break и active ordered structure на малых тестах |
| 3 | `Core` | [CSES - Area of Rectangles](https://cses.fi/problemset/task/1741) | - | Геометрический sweep и длина объединения активных y-интервалов |

<a id="practice-closest-pair"></a>

### 25.6. Пара ближайших точек

Этап **C**. Core: **2**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-closest-pair).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CSES - Minimum Euclidean Distance](https://cses.fi/problemset/task/2194) | - | Closest pair divide-and-conquer за `O(n log n)` |
| 2 | `Core` | Локальный checkpoint: closest pair | Checkpoint | Сохранение sort-by-y, strip и stress против `O(n^2)` |
| 3 | `Extra` | [Kattis - closestpair1](https://open.kattis.com/problems/closestpair1) | - | Восстановление самой пары и floating-point output |

<a id="practice-advanced-graphs"></a>

## Модуль 26. Структура графов

<a id="practice-scc"></a>

### 26.1. SCC и граф конденсации

Этап **B**. Core: **3**. Extra: **2**. Теория: [ROADMAP](ROADMAP.md#topic-scc).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CSES - Planets and Kingdoms](https://cses.fi/problemset/task/1683) | - | Kosaraju/Tarjan и номер SCC каждой вершины |
| 2 | `Core` | [CF 427C - Checkposts](https://codeforces.com/problemset/problem/427/C) | CF 1700 | SCC плюс минимум и число способов внутри компоненты |
| 3 | `Core` | [CSES - Coin Collector](https://cses.fi/problemset/task/1686) | - | Condensation DAG и DP максимальной суммы |
| 4 | `Extra` | [CF 999E - Reachability from the Capital](https://codeforces.com/problemset/problem/999/E) | CF 1800 | Истоки недостижимой части condensation |
| 5 | `Extra` | [CF 1239D - Catowice City](https://codeforces.com/problemset/problem/1239/D) | CF 2200 | SCC-подобное разбиение ориентированных отношений |

<a id="practice-two-sat"></a>

### 26.2. 2-SAT

Этап **B**. Core: **2**. Extra: **2**. Теория: [ROADMAP](ROADMAP.md#topic-two-sat).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CSES - Giant Pizza](https://cses.fi/problemset/task/1684) | - | Clauses, implication graph и восстановление assignment |
| 2 | `Core` | [CF 776D - The Door Problem](https://codeforces.com/problemset/problem/776/D) | CF 2200 | Равенство/неравенство двух булевых переменных как 2-SAT |
| 3 | `Extra` | [CF 468B - Two Sets](https://codeforces.com/problemset/problem/468/B) | CF 2100 | Выбор группы и импликации по необходимым дополнениям |
| 4 | `Extra` | [CF 27D - Ring Road 2](https://codeforces.com/problemset/problem/27/D) | CF 2400 | Геометрические конфликты хорд как булевы ограничения |

<a id="practice-bridges-edge-bcc"></a>

### 26.3. Мосты, 2-edge-components и bridge tree

Этап **B**. Core: **3**. Extra: **3**. Теория: [ROADMAP](ROADMAP.md#topic-bridges-edge-bcc).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 1192 - Critical Connections](https://leetcode.com/problems/critical-connections-in-a-network/) | LC Hard | Мосты через `tin/low` |
| 2 | `Core` | [CSES - Necessary Roads](https://cses.fi/problemset/task/2076) | - | Multigraph-safe поиск всех мостов по edge id |
| 3 | `Core` | [CF 1000E - We Need More Bosses](https://codeforces.com/problemset/problem/1000/E) | CF 2100 | 2-edge-components, bridge tree и диаметр |
| 4 | `Extra` | [CF 118E - Bertown Roads](https://codeforces.com/problemset/problem/118/E) | CF 2000 | Отсутствие мостов и сильная ориентация ребер |
| 5 | `Extra` | [CF 652E - Pursuit For Artifacts](https://codeforces.com/problemset/problem/652/E) | CF 2300 | Bridge tree и агрегат на пути |
| 6 | `Extra` | [CF 732F - Tourist Reform](https://codeforces.com/problemset/problem/732/F) | CF 2400 | 2-edge-components и ориентация для максимальной SCC |

<a id="practice-articulation-vertex-bcc"></a>

### 26.4. Точки сочленения, vertex-biconnected blocks и block-cut tree

Этап **B**. Core: **2**. Extra: **0**. Теория: [ROADMAP](ROADMAP.md#topic-articulation-vertex-bcc).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF Gym 100083D - Точки сочленения](https://codeforces.com/gym/100083/problem/D) | - | Условие `low >= tin`, root case и articulation points |
| 2 | `Core` | Локальный checkpoint: vertex-BCC и block-cut tree | Checkpoint | Edge stack, извлечение блоков и двудольное дерево блоков и точек сочленения |

<a id="practice-dsu-mst"></a>

## Модуль 27. Остовы и монотонная связность

<a id="practice-mst"></a>

### 27.1. Минимальные остовы

Этап **B**. Core: **5**. Extra: **6**. Теория: [ROADMAP](ROADMAP.md#topic-mst).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 1584 - Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | LC Medium | Dense Prim и полный граф расстояний |
| 2 | `Core` | [ACMP 142 - Минимальный каркас](https://acmp.ru/index.asp?main=task&id_task=142) | - | Базовый Kruskal + DSU |
| 3 | `Core` | Локальный checkpoint: sparse Prim | - | Heap, visited и disconnected graph |
| 4 | `Core` | [CF 1245D - Shichikuji and Power Grid](https://codeforces.com/problemset/problem/1245/D) | CF 1900 | Virtual source, Prim и восстановление сети |
| 5 | `Core` | [CF EDU 7.2E - Spanning Tree](https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E) | EDU | Kruskal и стоимость минимального остова |
| 6 | `Extra` | [CF 160D - Edges in MST](https://codeforces.com/problemset/problem/160/D) | CF 2300 | Группы равных весов и классификация ребер MST |
| 7 | `Extra` | [CF 609E - Minimum Spanning Tree for Each Edge](https://codeforces.com/problemset/problem/609/E) | CF 2100 | MST плюс maximum edge on path |
| 8 | `Extra` | [CF 1513D - GCD and MST](https://codeforces.com/problemset/problem/1513/D) | CF 1800 | Специальное построение дешевых ребер перед обычным Kruskal |
| 9 | `Extra` | [CF EDU 7.2F - Dense Spanning Tree](https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/F) | EDU | Минимальная ширина остова |
| 10 | `Extra` | [CF EDU 7.2G - No Refuel](https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/G) | EDU | Bottleneck-свойство остова |
| 11 | `Extra` | [CF EDU 7.2H - Oil Business](https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/H) | EDU | Maximum spanning forest и complement greedy |

<a id="practice-dsu-offline-activation"></a>

### 27.2. Офлайн-активация через DSU

Этап **B**. Core: **3**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-dsu-offline-activation).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: component size under threshold | - | Сортировка ребер и запросов с одинаковым порогом |
| 2 | `Core` | [CF 1213G - Path Queries](https://codeforces.com/problemset/problem/1213/G) | CF 1800 | Активация ребер по весу + metadata компонент |
| 3 | `Core` | [CF 722C - Destroying Array](https://codeforces.com/problemset/problem/722/C) | CF 1900 | Обратное время: удаления превращаются в добавления |
| 4 | `Extra` | [CF 1706E - Qpwoeirut And Vertices](https://codeforces.com/problemset/problem/1706/E) | CF 2100 | Kruskal reconstruction tree после монотонных union |

<a id="practice-advanced-dp"></a>

## Модуль 28. Продвинутое динамическое программирование

<a id="practice-interval-dp"></a>

### 28.1. DP по отрезкам

Этап **B**. Core: **3**. Теория: [ROADMAP](ROADMAP.md#topic-interval-dp).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 312 - Burst Balloons](https://leetcode.com/problems/burst-balloons/) | LC Hard | Выбрать последний элемент внутри отрезка |
| 2 | `Core` | [CF 607B - Zuma](https://codeforces.com/problemset/problem/607/B) | CF 1900 | Связать равные концы и объединить вложенные интервалы |
| 3 | `Core` | [AtCoder DP N - Slimes](https://atcoder.jp/contests/dp/tasks/dp_n) | - | Перебор последнего разбиения и prefix cost |

<a id="practice-layered-grid-dp"></a>

### 28.2. Слоистое DP по решетке и состояниям

Этап **B**. Core: **2**. Extra: **0**. Теория: [ROADMAP](ROADMAP.md#topic-layered-grid-dp).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 1695C - Zero Path](https://codeforces.com/problemset/problem/1695/C) | CF 1700 | Min/max достижимой суммы, длина и четность пути |
| 2 | `Core` | [CF 1517D - Explorer Space](https://codeforces.com/problemset/problem/1517/D) | CF 1800 | DP на точное число шагов и rolling layers |

<a id="practice-subtree-dp"></a>

### 28.3. DP по поддеревьям

Этап **B**. Core: **3**. Теория: [ROADMAP](ROADMAP.md#topic-subtree-dp).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 1528A - Parsa's Humongous Tree](https://codeforces.com/problemset/problem/1528/A) | CF 1600 | Два состояния вершины и независимый выбор детей |
| 2 | `Core` | [AtCoder DP P - Independent Set](https://atcoder.jp/contests/dp/tasks/dp_p) | - | take/skip на дереве |
| 3 | `Core` | [CF 161D - Distance in Tree](https://codeforces.com/problemset/problem/161/D) | CF 1800 | Merge распределений расстояний детей |

<a id="practice-rerooting"></a>

### 28.4. Rerooting DP

Этап **B**. Core: **4**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-rerooting).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 834 - Sum of Distances in Tree](https://leetcode.com/problems/sum-of-distances-in-tree/) | LC Hard | Размеры поддеревьев и перенос суммы через ребро |
| 2 | `Core` | [CF 1092F - Tree with Maximum Cost](https://codeforces.com/problemset/problem/1092/F) | CF 1900 | Взвешенный перенос ответа parent -> child |
| 3 | `Core` | [CF 1324F - Maximum White Subtree](https://codeforces.com/problemset/problem/1324/F) | CF 1800 | Down/up contributions с отсечением отрицательного |
| 4 | `Core` | [AtCoder DP V - Subtree](https://atcoder.jp/contests/dp/tasks/dp_v) | - | Общий rerooting через prefix/suffix merge |
| 5 | `Extra` | [CF 1187E - Tree Painting](https://codeforces.com/problemset/problem/1187/E) | CF 2100 | Вывод формулы rerooting для score |

<a id="practice-subset-dp"></a>

## Модуль 29. DP по компактным пространствам состояний

<a id="practice-subset-dp-core"></a>

### 29.1. DP по подмножествам

Этап **B**. Core: **4**. Extra: **2**. Теория: [ROADMAP](ROADMAP.md#topic-subset-dp-core).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 1066 - Campus Bikes II](https://leetcode.com/problems/campus-bikes-ii/) | LC Medium | `dp[mask]` для назначения первых работников |
| 2 | `Core` | [CF 580D - Kefa and Dishes](https://codeforces.com/problemset/problem/580/D) | CF 1800 | `dp[mask][last]` с бонусом порядка |
| 3 | `Core` | [CSES - Elevator Rides](https://cses.fi/problemset/task/1653) | - | Лексикографическое состояние: число групп и остаток |
| 4 | `Core` | [CSES - Hamiltonian Flights](https://cses.fi/problemset/task/1690) | - | Пути по маске посещенных вершин и последней вершине |
| 5 | `Extra` | [CF 8C - Looking for Order](https://codeforces.com/problemset/problem/8/C) | CF 2000 | Переход по паре и восстановление |
| 6 | `Extra` | [AtCoder DP O - Matching](https://atcoder.jp/contests/dp/tasks/dp_o) | - | Назначение по числу битов mask |

<a id="practice-digit-dp"></a>

### 29.2. Digit DP

Этап **B**. Core: **4**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-digit-dp).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 902 - Numbers At Most N Given Digit Set](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/) | LC Hard | Вводный tight/started по разрешенным цифрам |
| 2 | `Core` | [CF 1036C - Classy Numbers](https://codeforces.com/problemset/problem/1036/C) | CF 1900 | `count(0..x)` и ограничение числа ненулевых цифр |
| 3 | `Core` | [CSES - Counting Numbers](https://cses.fi/problemset/task/2220) | - | Предыдущая цифра, leading zeros и диапазон |
| 4 | `Core` | [CF 628D - Magic Numbers](https://codeforces.com/problemset/problem/628/D) | CF 2200 | Tight, позиционное правило и остаток по модулю |
| 5 | `Extra` | [CF 55D - Beautiful numbers](https://codeforces.com/problemset/problem/55/D) | CF 2500 | LCM цифр и сжатое состояние остатка |

<a id="practice-profile-dp"></a>

### 29.3. Profile DP

Этап **B**. Core: **3**. Теория: [ROADMAP](ROADMAP.md#topic-profile-dp).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: domino tilings | - | Заполнение первой свободной клетки профиля |
| 2 | `Core` | [CSES - Counting Tilings](https://cses.fi/problemset/task/2181) | - | Генерация совместимых масок соседних столбцов |
| 3 | `Core` | [CF 1391D - 505](https://codeforces.com/problemset/problem/1391/D) | CF 2000 | Совместимость масок и выбор малой размерности |

<a id="practice-sos-dp"></a>

### 29.4. SOS DP

Этап **C**. Core: **3**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-sos-dp).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: subset/superset zeta and Mobius | - | Оба направления преобразования и обратимость |
| 2 | `Core` | [CSES - Bit Problem](https://cses.fi/problemset/task/1654) | - | Число подмасок, надмасок и масок с непустым AND |
| 3 | `Core` | [CF 165E - Compatible Numbers](https://codeforces.com/problemset/problem/165/E) | CF 2200 | Распространение свидетеля по подмаскам complement |
| 4 | `Extra` | [CF 449D - Jzzhu and Numbers](https://codeforces.com/problemset/problem/449/D) | CF 2400 | SOS + inclusion-exclusion для AND подмножеств |

<a id="practice-treap"></a>

## Модуль 30. Декартовы деревья и порядковые структуры

<a id="practice-cartesian-tree"></a>

### 30.1. Статическое декартово дерево

Этап **B**. Core: **2**. Теория: [ROADMAP](ROADMAP.md#topic-cartesian-tree).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: Cartesian tree in O(n) | - | Монотонный стек, parent/left/right и inorder |
| 2 | `Core` | [CF 1748E - Yet Another Array Counting Problem](https://codeforces.com/problemset/problem/1748/E) | CF 2400 | Дерево максимумов и DP по его форме |

<a id="practice-explicit-treap"></a>

### 30.2. Explicit-key treap

Этап **B**. Core: **3**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-explicit-treap).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: ordered multiset | - | insert/erase/kth/rank через split/merge и size |
| 2 | `Core` | [CSES - Salary Queries](https://cses.fi/problemset/task/1144) | - | Treap по ключу с multiplicity и count on range |
| 3 | `Core` | Локальный checkpoint: range sum by explicit key | - | Два split по ключам и агрегат subtree sum |
| 4 | `Extra` | [CF 702F - T-Shirts](https://codeforces.com/problemset/problem/702/F) | CF 2400 | Treap, lazy и нетривиальное разбиение по ключу |

<a id="practice-implicit-treap"></a>

### 30.3. Implicit treap

Этап **B**. Core: **3**. Extra: **2**. Теория: [ROADMAP](ROADMAP.md#topic-implicit-treap).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: sequence editor | - | split by size, insert, erase и reverse |
| 2 | `Core` | [CSES - Reversals and Sums](https://cses.fi/problemset/task/2074) | - | Lazy reverse и subtree sum |
| 3 | `Core` | [CF Gym 102787A - Cut and Paste](https://codeforces.com/gym/102787/problem/A) | - | Вырезание и склейка сегментов split/merge |
| 4 | `Extra` | [CF Gym 102787B - To Front or Not to Front](https://codeforces.com/gym/102787/problem/B) | - | Перестановки блоков последовательности |
| 5 | `Extra` | [CF Gym 102787E - Yet Another Array Queries Problem](https://codeforces.com/gym/102787/problem/E) | - | Составные lazy-операции на отрезке |

<a id="practice-bitwise-trie"></a>

### 30.4. Bitwise trie

Этап **B**. Core: **3**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-bitwise-trie).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: dynamic max XOR multiset | - | insert/delete/query и count в узлах |
| 2 | `Core` | [CF 706D - Vasiliy's Multiset](https://codeforces.com/problemset/problem/706/D) | CF 1800 | Online multiset и greedy по битам |
| 3 | `Core` | [CSES - Maximum Xor Subarray](https://cses.fi/problemset/task/1655) | - | Trie префиксных XOR |
| 4 | `Extra` | [CF 923C - Perfect Security](https://codeforces.com/problemset/problem/923/C) | CF 2000 | Min XOR matching с удалением |

<a id="practice-flows-matching"></a>

## Модуль 31. Паросочетания и потоки

<a id="practice-bipartite-matching"></a>

### 31.1. Двудольное паросочетание

Этап **B**. Core: **4**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-bipartite-matching).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 1820 - Maximum Number of Accepted Invitations](https://leetcode.com/problems/maximum-number-of-accepted-invitations/) | LC Medium | Чистый augmenting path |
| 2 | `Core` | Локальный checkpoint: Hopcroft-Karp | - | BFS layers + DFS blocking augmentations |
| 3 | `Core` | [CF 120H - Red and Blue Balls](https://codeforces.com/problemset/problem/120/H) | CF 1900 | Построение двудольного графа допустимости |
| 4 | `Core` | [CF 1423B - Valuable Paper](https://codeforces.com/problemset/problem/1423/B) | CF 2100 | Binary search threshold + perfect matching |
| 5 | `Extra` | [CSES - School Dance](https://cses.fi/problemset/task/1696) | - | Реализация matching через flow и сравнение подходов |

<a id="practice-max-flow"></a>

### 31.2. Максимальный поток и минимальный разрез

Этап **B**. Core: **4**. Extra: **2**. Теория: [ROADMAP](ROADMAP.md#topic-max-flow).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CSES - Download Speed](https://cses.fi/problemset/task/1694) | - | Чистый Dinic на capacities |
| 2 | `Core` | [CF 546E - Soldier and Traveling](https://codeforces.com/problemset/problem/546/E) | CF 2100 | Матрица перемещений как flow construction |
| 3 | `Core` | [CSES - Distinct Routes](https://cses.fi/problemset/task/1711) | - | Edge-disjoint paths и декомпозиция потока |
| 4 | `Core` | [CSES - Police Chase](https://cses.fi/problemset/task/1695) | - | Min-cut edges по достижимости residual graph |
| 5 | `Extra` | [CF 510E - Fox And Dinner](https://codeforces.com/problemset/problem/510/E) | CF 2300 | Degree constraints, flow и восстановление циклов |
| 6 | `Extra` | [CF 1082G - Petya and Graph](https://codeforces.com/problemset/problem/1082/G) | CF 2400 | Maximum-weight closure через min-cut |

<a id="practice-min-cost-flow"></a>

### 31.3. Поток минимальной стоимости

Этап **C**. Core: **2**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-min-cost-flow).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: assignment with costs | - | Successive shortest augmenting paths + potentials |
| 2 | `Core` | [AtCoder Library Practice E - MinCostFlow](https://atcoder.jp/contests/practice2/tasks/practice2_e) | - | Моделирование выбора клеток через min-cost flow |
| 3 | `Extra` | [CF 237E - Build String](https://codeforces.com/problemset/problem/237/E) | CF 2300 | Ограниченные источники символов и стоимость использования |

<a id="practice-advanced-strings"></a>

## Модуль 32. Продвинутые строковые структуры

<a id="practice-aho-corasick"></a>

### 32.1. Ахо-Корасик

Этап **B**. Core: **3**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-aho-corasick).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CSES - Finding Patterns](https://cses.fi/problemset/task/2102) | - | Multi-pattern existence через автомат |
| 2 | `Core` | [CSES - Counting Patterns](https://cses.fi/problemset/task/2103) | - | Накопление посещений по suffix links |
| 3 | `Core` | [CF 1202E - You Are Given Some Strings](https://codeforces.com/problemset/problem/1202/E) | CF 2400 | Два автомата и склейка совпадений |
| 4 | `Extra` | [CF 710F - String Set Queries](https://codeforces.com/problemset/problem/710/F) | CF 2500 | Динамический набор через logarithmic rebuilding автоматов |

<a id="practice-manacher"></a>

### 32.2. Алгоритм Манакера

Этап **B**. Core: **2**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-manacher).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CSES - Longest Palindrome](https://cses.fi/problemset/task/1111) | - | Odd/even radii и восстановление максимума |
| 2 | `Core` | [CSES - All Palindromes](https://cses.fi/problemset/task/3138) | - | Вывод всех длин из массивов радиусов |
| 3 | `Extra` | [CF 1326D2 - Prefix-Suffix Palindrome](https://codeforces.com/problemset/problem/1326/D2) | CF 1800 | Палиндром внутри остатка; решить именно Манакером |

<a id="practice-suffix-array"></a>

### 32.3. Suffix array и LCP

Этап **B**. Core: **4**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-suffix-array).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: suffix array + Kasai | - | Doubling, counting sort и LCP против brute force |
| 2 | `Core` | [CSES - Repeating Substring](https://cses.fi/problemset/task/2106) | - | Максимальный соседний LCP |
| 3 | `Core` | [CSES - Pattern Positions](https://cses.fi/problemset/task/2104) | - | Binary search диапазона суффиксов |
| 4 | `Core` | [CF 19C - Deletion of Repeats](https://codeforces.com/problemset/problem/19/C) | CF 2400 | LCP/RMQ и обнаружение повторяющихся блоков |
| 5 | `Extra` | [CF 123D - String](https://codeforces.com/problemset/problem/123/D) | CF 2900 | Contribution counting по LCP structure |

<a id="practice-suffix-automaton"></a>

### 32.4. Суффиксный автомат

Этап **C**. Core: **3**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-suffix-automaton).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: SAM extend/clone | - | Сравнение множества подстрок с brute force |
| 2 | `Core` | [CSES - Distinct Substrings](https://cses.fi/problemset/task/2105) | - | Сумма `len[v] - len[link[v]]` |
| 3 | `Core` | [CSES - Substring Order I](https://cses.fi/problemset/task/2108) | - | DP числа путей и k-я подстрока |
| 4 | `Extra` | [CF 873F - Forbidden Indices](https://codeforces.com/problemset/problem/873/F) | CF 2400 | Occurrence propagation и лучший state contribution |

<a id="practice-advanced-trees"></a>

## Модуль 33. Декомпозиции деревьев

<a id="practice-hld"></a>

### 33.1. Heavy-light decomposition

Этап **B**. Core: **2**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-hld).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: path sum with point updates | - | `head/pos`, разложение пути и segment tree |
| 2 | `Core` | [CSES - Path Queries II](https://cses.fi/problemset/task/2134) | - | Point update + maximum on path |
| 3 | `Extra` | [CF 593D - Happy Tree Party](https://codeforces.com/problemset/problem/593/D) | CF 2200 | Направленный проход по цепочкам и ранний stop |

<a id="practice-centroid-decomposition"></a>

### 33.2. Центроидная декомпозиция

Этап **B**. Core: **2**. Extra: **2**. Теория: [ROADMAP](ROADMAP.md#topic-centroid-decomposition).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 321C - Ciel the Commander](https://codeforces.com/problemset/problem/321/C) | CF 1900 | Чистое построение centroid tree |
| 2 | `Core` | [CF 342E - Xenia and Tree](https://codeforces.com/problemset/problem/342/E) | CF 2400 | Dynamic nearest marked node по centroid ancestors |
| 3 | `Extra` | [CSES - Fixed-Length Paths I](https://cses.fi/problemset/task/2080) | - | Подсчет путей через centroid |
| 4 | `Extra` | [CF 161D - Distance in Tree](https://codeforces.com/problemset/problem/161/D) | CF 1800 | Решить повторно через centroid и сравнить с subtree DP |

<a id="practice-small-to-large"></a>

### 33.3. Small-to-large merge контейнеров

Этап **B**. Core: **2**. Extra: **0**. Теория: [ROADMAP](ROADMAP.md#topic-small-to-large).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CSES - Distinct Colors](https://cses.fi/problemset/task/1139) | - | Merge smaller color set into larger |
| 2 | `Core` | Локальный checkpoint: frequency maps in every subtree | - | Амортизация перемещений элементов |

<a id="practice-dsu-on-tree"></a>

### 33.4. Sack и DSU on tree

Этап **B**. Core: **2**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-dsu-on-tree).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 600E - Lomsat Gelral](https://codeforces.com/problemset/problem/600/E) | CF 2300 | Сохранить данные heavy child и переиграть light subtrees |
| 2 | `Core` | [CF 375D - Tree and Queries](https://codeforces.com/problemset/problem/375/D) | CF 2300 | Sack с частотами частот |
| 3 | `Extra` | Локальный checkpoint: sack lifecycle | Checkpoint | `addSubtree`, `keep`, очистка light subtree и stress против обычного DFS |

<a id="practice-games"></a>

## Модуль 34. Теория игр

<a id="practice-pn-games"></a>

### 34.1. P/N-позиции

Этап **B**. Core: **2**. Extra: **2**. Теория: [ROADMAP](ROADMAP.md#topic-pn-games).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 292 - Nim Game](https://leetcode.com/problems/nim-game/) | LC Easy | Subtraction game 1..3 и проигрышные кратные 4; не Nim-sum |
| 2 | `Core` | [CF 1033C - Permutation Game](https://codeforces.com/problemset/problem/1033/C) | CF 1800 | Retrograde по ацикличному порядку значений |
| 3 | `Extra` | [CF 1194D - 1-2-K Game](https://codeforces.com/problemset/problem/1194/D) | CF 1900 | Период P/N-позиций с отдельным случаем `k` |
| 4 | `Extra` | [CF 455B - A Lot of Games](https://codeforces.com/problemset/problem/455/B) | CF 1900 | Два типа terminal condition на trie игры |

<a id="practice-minimax"></a>

### 34.2. Minimax

Этап **B**. Core: **1**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-minimax).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 486 - Predict the Winner](https://leetcode.com/problems/predict-the-winner/) | LC Medium | Interval minimax по разнице счета |
| 2 | `Extra` | [LC 464 - Can I Win](https://leetcode.com/problems/can-i-win/) | LC Medium | Minimax + memoization по mask |

<a id="practice-nim-sg"></a>

### 34.3. Nim и Sprague-Grundy

Этап **B**. Core: **3**. Extra: **2**. Теория: [ROADMAP](ROADMAP.md#topic-nim-sg).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: true Nim | - | XOR куч, выигрышный ход и доказательство |
| 2 | `Core` | Локальный checkpoint: Grundy on DAG | - | `mex` исходящих состояний и XOR компонент |
| 3 | `Core` | [CF 15C - Industrial Nim](https://codeforces.com/problemset/problem/15/C) | CF 2100 | Nim-sum диапазонов без перечисления куч |
| 4 | `Extra` | [CF 768E - Game of Stones](https://codeforces.com/problemset/problem/768/E) | CF 2300 | Grundy ограниченного разбиения куч |
| 5 | `Extra` | [CF 850C - Arpa and a game of Mojtaba](https://codeforces.com/problemset/problem/850/C) | CF 2400 | Независимые компоненты по простым и SG mask states |

<a id="practice-cyclic-games"></a>

### 34.4. Игры с циклами

Этап **C**. Core: **2**. Теория: [ROADMAP](ROADMAP.md#topic-cyclic-games).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: win/lose/draw on directed graph | - | Reverse edges, outdegree counter и неразмеченные ничьи |
| 2 | `Core` | [CF 786A - Berzerk](https://codeforces.com/problemset/problem/786/A) | CF 2100 | Retrograde двух игроков на циклических состояниях |

<a id="practice-meet-in-the-middle"></a>

## 35. Meet-in-the-middle

Этап **B**. Core: **4**. Extra: **2**. Теория: [ROADMAP](ROADMAP.md#topic-meet-in-the-middle).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 1755 - Closest Subsequence Sum](https://leetcode.com/problems/closest-subsequence-sum/) | LC Hard | Две половины subset sums + binary search |
| 2 | `Core` | [CSES - Meet in the Middle](https://cses.fi/problemset/task/1628) | - | Подсчет пар half-sums с заданной суммой |
| 3 | `Core` | [CF 888E - Maximum Subsequence](https://codeforces.com/problemset/problem/888/E) | CF 1800 | Максимум суммы по модулю из двух половин |
| 4 | `Core` | [CF 1006F - Xor-Paths](https://codeforces.com/problemset/problem/1006/F) | CF 2100 | Разбиение пути по средней диагонали |
| 5 | `Extra` | [CF 525E - Anya and Cubes](https://codeforces.com/problemset/problem/525/E) | CF 2200 | Три выбора элемента и count maps половин |
| 6 | `Extra` | [AtCoder ABC184F - Programming Contest](https://atcoder.jp/contests/abc184/tasks/abc184_f) | - | Максимальная subset sum не больше `T` из двух half-lists |

<a id="practice-sqrt-mo"></a>

## Модуль 36. Корневая декомпозиция запросов

<a id="practice-sqrt-blocks"></a>

### 36.1. Блочные агрегаты и обновления

Этап **C**. Core: **3**. Extra: **0**. Теория: [ROADMAP](ROADMAP.md#topic-sqrt-blocks).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: point update + range sum | - | Полные и краевые блоки |
| 2 | `Core` | Локальный checkpoint: range add + range sum | - | Lazy tag и агрегат блока |
| 3 | `Core` | Локальный checkpoint: count values below x | - | Sorted blocks и пересборка после update |

<a id="practice-sqrt-jump"></a>

### 36.2. Jump pointers с блочной пересборкой

Этап **C**. Core: **1**. Extra: **0**. Теория: [ROADMAP](ROADMAP.md#topic-sqrt-jump).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 13E - Holes](https://codeforces.com/problemset/problem/13/E) | CF 2200 | Jump pointers внутри блока и локальная пересборка после update |

<a id="practice-dynamic-blocks"></a>

### 36.3. Динамическая последовательность блоками

Этап **C**. Core: **1**. Extra: **0**. Теория: [ROADMAP](ROADMAP.md#topic-dynamic-blocks).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 455D - Serega and Fun](https://codeforces.com/problemset/problem/455/D) | CF 2600 | Перемещение элементов и частоты внутри динамических блоков |

<a id="practice-small-large-heuristics"></a>

### 36.4. Разделение параметра на малый и большой

Этап **C**. Core: **1**. Extra: **0**. Теория: [ROADMAP](ROADMAP.md#topic-small-large-heuristics).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 1207F - Remainder Problem](https://codeforces.com/problemset/problem/1207/F) | CF 2100 | Предподсчет малых модулей и прямой проход по большим |

<a id="practice-mo"></a>

### 36.5. Алгоритм Мо

Этап **C**. Core: **3**. Extra: **2**. Теория: [ROADMAP](ROADMAP.md#topic-mo).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CSES - Distinct Values Queries](https://cses.fi/problemset/task/1734) | - | Реализовать именно Mo: add/remove и distinct count |
| 2 | `Core` | Локальный checkpoint: Mo vs brute stress | - | Четыре движения границ и alternating order |
| 3 | `Core` | [CF 86D - Powerful array](https://codeforces.com/problemset/problem/86/D) | CF 2200 | Нетривиальный вклад частоты при add/remove |
| 4 | `Extra` | [CF 617E - XOR and Favorite Number](https://codeforces.com/problemset/problem/617/E) | CF 2200 | Mo по префиксным XOR |
| 5 | `Extra` | [CF 940F - Machine Learning](https://codeforces.com/problemset/problem/940/F) | CF 2600 | Mo with modifications и mex частот |

<a id="practice-rollback-persistence"></a>

## Модуль 37. Версии структур и динамическая связность

<a id="practice-version-rollback"></a>

### 37.1. Rollback по дереву версий

Этап **C**. Core: **2**. Теория: [ROADMAP](ROADMAP.md#topic-version-rollback).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: version tree + undo log | - | Snapshot, apply, DFS и точный rollback |
| 2 | `Core` | [CF 707D - Persistent Bookcase](https://codeforces.com/problemset/problem/707/D) | CF 2200 | Дерево версий запросов и отмена изменений |

<a id="practice-persistence"></a>

### 37.2. Персистентные структуры

Этап **C**. Core: **2**. Extra: **2**. Теория: [ROADMAP](ROADMAP.md#topic-persistence).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Extra` | [LC 1146 - Snapshot Array](https://leetcode.com/problems/snapshot-array/) | LC Medium | Per-index история значений и binary search по времени; не path copying |
| 2 | `Core` | [CSES - Range Queries and Copies](https://cses.fi/problemset/task/1737) | - | Path-copying segment tree и roots версий |
| 3 | `Core` | [CF 813E - Army Creation](https://codeforces.com/problemset/problem/813/E) | CF 2200 | Persistent segment tree по префиксам |
| 4 | `Extra` | [CF 484E - Sign on Fence](https://codeforces.com/problemset/problem/484/E) | CF 2600 | Версии по порогу плюс binary search answer |

<a id="practice-rollback-dsu"></a>

### 37.3. Rollback DSU

Этап **C**. Core: **2**. Extra: **0**. Теория: [ROADMAP](ROADMAP.md#topic-rollback-dsu).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: RollbackDSU | - | Union by size без path compression, snapshot и undo |
| 2 | `Core` | [CF 891C - Envy](https://codeforces.com/problemset/problem/891/C) | CF 2600 | Временные union групп запросов и точный rollback |

<a id="practice-dynamic-connectivity"></a>

### 37.4. Segment tree over time и dynamic connectivity

Этап **C**. Core: **1**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-dynamic-connectivity).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CSES - Dynamic Connectivity](https://cses.fi/problemset/task/2133) | - | Интервалы жизни ребер плюс segment tree over time |
| 2 | `Extra` | [CF 1140F - Extending Set of Points](https://codeforces.com/problemset/problem/1140/F) | CF 2700 | Dynamic bipartite components и rollback metadata |

<a id="practice-dp-optimizations"></a>

## Модуль 38. Оптимизации DP

<a id="practice-monotone-cht"></a>

### 38.1. Monotone CHT

Этап **B**. Core: **2**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-monotone-cht).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: monotone CHT | Checkpoint | Вывести формулу прямой, обработать равные slopes и сверить с `O(n^2)` |
| 2 | `Core` | [CF 319C - Kalila and Dimna in the Logging Industry](https://codeforces.com/problemset/problem/319/C) | CF 2100 | Монотонные slopes и query coordinates |
| 3 | `Extra` | [CF 660F - Bear and Bowling 4](https://codeforces.com/problemset/problem/660/F) | CF 2400 | Монотонные slopes, произвольные `x`, hull плюс binary search |

<a id="practice-li-chao"></a>

### 38.2. Li Chao Tree

Этап **C**. Core: **1**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-li-chao).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CSES - Monster Game II](https://cses.fi/problemset/task/2085) | - | Произвольные slopes и `x`, online add/query |
| 2 | `Extra` | [CF 932F - Escape Through Leaf](https://codeforces.com/problemset/problem/932/F) | CF 2600 | Tree DP + small-to-large line containers |

<a id="practice-divide-conquer-dp"></a>

### 38.3. Divide-and-conquer optimization DP

Этап **C**. Core: **2**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-divide-conquer-dp).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: D&C optimization | Checkpoint | Сравнить слой с `O(kn^2)`, проверить monotone opt и границы рекурсии |
| 2 | `Core` | [CF 321E - Ciel and Gondolas](https://codeforces.com/problemset/problem/321/E) | CF 2600 | Monotone opt и `O(1)` cost через 2D prefix sums |
| 3 | `Extra` | [CF 868F - Yet Another Minimization Problem](https://codeforces.com/problemset/problem/868/F) | CF 2500 | D&C optimization плюс подвижная стоимость окна |

<a id="practice-knuth"></a>

### 38.4. Оптимизация Кнута

Этап **C**. Core: **2**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-knuth).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: Knuth optimization | Checkpoint | Сравнить с `O(n^3)` и проверить `opt[l][r-1] <= opt[l][r] <= opt[l+1][r]` |
| 2 | `Core` | [CSES - Knuth Division](https://cses.fi/problemset/task/2088) | - | Каноническое interval DP и границы opt |
| 3 | `Extra` | [CF Gym 100212C - Order-Preserving Codes](https://codeforces.com/gym/100212/problem/C) | - | Knuth плюс моделирование и восстановление кодов |

<a id="practice-linear-algebra-fft"></a>

## Модуль 39. Алгебраические алгоритмы

<a id="practice-matrix-exponentiation"></a>

### 39.1. Матричное возведение

Этап **C**. Core: **3**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-matrix-exponentiation).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: matrix power vs repeated multiplication | - | Identity, `M^0`, `M^k` и модуль |
| 2 | `Core` | [CSES - Throwing Dice](https://cses.fi/problemset/task/1096) | - | Линейная рекуррентность как матрица перехода |
| 3 | `Core` | [CSES - Graph Paths I](https://cses.fi/problemset/task/1723) | - | Число путей ровно из `k` ребер |
| 4 | `Extra` | [CF 222E - Decoding Genome](https://codeforces.com/problemset/problem/222/E) | CF 2100 | Автомат запрещенных пар + matrix exponentiation |

<a id="practice-gaussian-elimination"></a>

### 39.2. Метод Гаусса и GF(2)

Этап **C**. Core: **3**. Теория: [ROADMAP](ROADMAP.md#topic-gaussian-elimination).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [ACMP 198 - Система линейных уравнений](https://acmp.ru/index.asp?main=task&id_task=198) | - | Плотный Гаусс с единственным решением |
| 2 | `Core` | [CSES - System of Linear Equations](https://cses.fi/problemset/task/3154) | - | Прямоугольная система modulo prime, none/free solutions |
| 3 | `Core` | [Timus 1042 - Central Heating](https://acm.timus.ru/problem.aspx?space=1&num=1042&locale=ru) | - | Гаусс над GF(2) и восстановление XOR-решения |

<a id="practice-xor-basis"></a>

### 39.3. Линейный XOR-базис

Этап **C**. Core: **2**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-xor-basis).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: insert/rank/represent/max XOR | - | Stress против полного перебора подмножеств |
| 2 | `Core` | [SPOJ XMAX - XOR Maximization](https://www.spoj.com/problems/XMAX/) | - | Максимальный subset XOR через basis |
| 3 | `Extra` | [CF 1101G - (Zero XOR Subset)-less](https://codeforces.com/problemset/problem/1101/G) | CF 2300 | Базис prefix XOR и дополнительное моделирование |

<a id="practice-convolution"></a>

### 39.4. Свертка, FFT и NTT

Этап **C**. Core: **4**. Extra: **2**. Теория: [ROADMAP](ROADMAP.md#topic-convolution).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: complex FFT | Checkpoint | `double[] re/im`, inverse, округление и stress против `O(nm)` на безопасных коэффициентах |
| 2 | `Core` | Локальный checkpoint: NTT stress | Checkpoint | Padding, inverse root и сравнение с `O(nm)` modulo `998244353` |
| 3 | `Core` | [CSES - Apples and Bananas](https://cses.fi/problemset/task/2111) | - | Частоты парных сумм как convolution |
| 4 | `Core` | [Library Checker - Convolution Mod](https://judge.yosupo.jp/problem/convolution_mod) | - | Самостоятельная NTT modulo `998244353` |
| 5 | `Extra` | [CF 1096G - Lucky Tickets](https://codeforces.com/problemset/problem/1096/G) | CF 2300 | Generating function и быстрое возведение полинома |
| 6 | `Extra` | [CF 528D - Fuzzy Search](https://codeforces.com/problemset/problem/528/D) | CF 2500 | Корреляция строк через несколько сверток |

<a id="practice-probability-interactive"></a>

## Модуль 40. Вероятность, рандомизация и специальные форматы

<a id="practice-probability"></a>

### 40.1. Вероятность и математическое ожидание

Этап **B**. Core: **5**. Теория: [ROADMAP](ROADMAP.md#topic-probability).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 453A - Little Pony and Expected Maximum](https://codeforces.com/problemset/problem/453/A) | CF 1600 | CDF максимума и tail-sum expectation |
| 2 | `Core` | [CF 839C - Journey](https://codeforces.com/problemset/problem/839/C) | CF 1500 | Условное ожидание по дереву |
| 3 | `Core` | [CSES - Inversion Probability](https://cses.fi/problemset/task/1728) | - | Индикаторы и линейность ожидания |
| 4 | `Core` | [CF 148D - Bag of mice](https://codeforces.com/problemset/problem/148/D) | CF 1800 | Probability DP по состоянию мешка и очередности |
| 5 | `Core` | [AtCoder DP J - Sushi](https://atcoder.jp/contests/dp/tasks/dp_j) | - | Expectation DP с self-loop и переносом члена |

<a id="practice-randomized"></a>

### 40.2. Рандомизированные алгоритмы

Этап **C**. Core: **2**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-randomized).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: randomized fingerprint | - | Fixed seed stress, collision event и global failure budget |
| 2 | `Core` | [CF 869E - The Untended Antiquity](https://codeforces.com/problemset/problem/869/E) | CF 2400 | 2D Fenwick + randomized set fingerprint |
| 3 | `Extra` | Локальный checkpoint: Karger min-cut | - | Monte Carlo success bound и amplification |

<a id="practice-interactive"></a>

### 40.3. Интерактивные задачи

Этап **C**. Core: **1**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-interactive).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: hidden number interactor | - | Binary search, flush, transcript и `ceil(log2 N)` запросов |
| 2 | `Extra` | [CF 1114E - Arithmetic Progression](https://codeforces.com/problemset/problem/1114/E) | CF 2200 | Interactive плюс binary search и randomized sampling |

<a id="practice-communication"></a>

### 40.4. Communication и double-run

Этап **C**. Core: **3**. Теория: [ROADMAP](ROADMAP.md#topic-communication).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [СПбГУ 2023/24, задача C](contests/03-spbu/2023-2024/final-statements.pdf) | - | Две изолированные фазы и ограниченное сообщение |
| 2 | `Core` | [СПбГУ 2024/25, задача A](contests/03-spbu/2024-2025/final-statements.pdf) | - | Double-run: encode/decode и лимит информации |
| 3 | `Core` | [СПбГУ 2025/26, задача C](contests/03-spbu/2025-2026/final/statements.pdf) | - | Communication wrapper и exhaustive stress |

<a id="practice-scored-constructive"></a>

### 40.5. Batch constructive со scoring

Этап **C**. Core: **1**. Теория: [ROADMAP](ROADMAP.md#topic-scored-constructive).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [МОШ 2025/26, задача B, этапы B1/B2](contests/14-moscow/2025-2026/final/full-with-answers-checkers.zip) | - | Valid baseline, затем улучшение score локальным checker и constructive heuristic |

<a id="practice-open-test-batch"></a>

### 40.7. Open-test Batch

Этап **C**. Core: **1**. Теория: [ROADMAP](ROADMAP.md#topic-open-test-batch).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [СПбГУ 2024/25, задача B](contests/03-spbu/2024-2025/final-statements.pdf) | - | Открытые inputs, но submission остается программой |
