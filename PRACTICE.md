# Банк задач

Этот каталог построен под календарь `лето -> отборы в октябре-ноябре -> финалы в марте-апреле`. Внутри каждой темы
задачи уже расположены в учебном порядке: от первого знакомства с приемом до более сложного переноса идеи.

## Объём и маршрут

- этап A0: **38 Core** и **25 Extra** - инженерная и алгоритмическая база;
- этап A1: **118 Core** и **109 Extra** - основные переносимые олимпиадные паттерны;
- этап B: **100 Core** и **44 Extra** - регулярный финальный слой;
- этап C: **53 Core** и **22 Extra** - выборочная продвинутая практика;
- полный каталог: **309 Core** и **200 Extra**, всего **509** строк;
- задачи внешних онлайн-судей: **457**, включая **59** задач LeetCode;
- локальные checkpoints: **46**; еще **6** строк используют официальные архивы олимпиад из `contests/`.

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

Этап **A0**. Core: **5**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: priority queue](ROADMAP.md#topic-priority-queue).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 703 - Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | LC Easy | heap из лучших `k` элементов |
| 2 | `Core` | [CF 1800C2 - Powering the Hero](https://codeforces.com/problemset/problem/1800/C2) | CF 1100 | Добавление бонусов в max-heap и извлечение лучшего по событию |
| 3 | `Core` | [CF Gym 102961T - Room Allocation](https://codeforces.com/gym/102961/problem/T) | - | Переиспользование ресурса с минимальным временем освобождения |
| 4 | `Core` | [CF 1353D - Constructing the Array](https://codeforces.com/problemset/problem/1353/D) | CF 1600 | Составной comparator: длина по убыванию, левая граница по возрастанию |
| 5 | `Core` | [CF 1468C - Berpizza](https://codeforces.com/problemset/problem/1468/C) | CF 1700 | Max-heap плюс FIFO/pointer, `served[]` и пропуск stale entries |
| 6 | `Extra` | [CF 1526C2 - Potions](https://codeforces.com/problemset/problem/1526/C2) | CF 1600 | Tentative selection и удаление худшего выбранного элемента |
| 7 | `Extra` | [LC 973 - K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | LC Medium | Heap размера `k`; это selection, а не вычислительная геометрия |

<a id="practice-prefix-difference-2d"></a>

## Модуль 7. Префиксные преобразования

<a id="practice-prefix-sums"></a>

### 7.1. Префиксные суммы и 2D-префиксы

Этап **A1**. Core: **5**. Extra: **1**. Теория и признаки распознавания: [ROADMAP: префиксные суммы](ROADMAP.md#topic-prefix-sums).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 303 - Range Sum Query Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | LC Easy | 1D-prefix |
| 2 | `Core` | [LC 304 - Range Sum Query 2D Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) | LC Medium | 2D-prefix |
| 3 | `Core` | [CF 1722E - Counting Rectangles](https://codeforces.com/problemset/problem/1722/E) | CF 1600 | Взвешенный 2D-prefix и строгие границы прямоугольного запроса |
| 4 | `Core` | [CF 466C - Number of Ways](https://codeforces.com/problemset/problem/466/C) | CF 1700 | Подсчет упорядоченных пар точек разбиения по значениям префикса |
| 5 | `Core` | Локальный checkpoint: prefix API | Checkpoint | 1D sum/xor/count и 2D rectangle sum на полуинтервалах; stress против прямого подсчета |
| 6 | `Extra` | [CF 1807D - Odd Queries](https://codeforces.com/problemset/problem/1807/D) | CF 900 | Префиксная сумма и виртуальная замена одного диапазона |

<a id="practice-difference-array"></a>

### 7.2. Массив разностей и офлайн-обновления диапазонов

Этап **A1**. Core: **3**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: массив разностей](ROADMAP.md#topic-difference-array).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 816B - Karen and Coffee](https://codeforces.com/problemset/problem/816/B) | CF 1400 | Difference array покрытия плюс prefix по готовому предикату |
| 2 | `Core` | [CF 295A - Greg and Array](https://codeforces.com/problemset/problem/295/A) | CF 1400 | Два вложенных уровня offline difference arrays |
| 3 | `Core` | Локальный checkpoint: range add offline | Checkpoint | `diff[l] += x`, `diff[r] -= x`, sentinel и восстановление на случайных полуинтервалах |
| 4 | `Extra` | [CF 276C - Little Girl and Maximum Sum](https://codeforces.com/problemset/problem/276/C) | CF 1500 | Частоты покрытия через differences плюс перестановочный greedy |
| 5 | `Extra` | [CF 1795C - Tea Tasting](https://codeforces.com/problemset/problem/1795/C) | CF 1500 | Difference array полных вкладов плюс один частичный край |

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

## 12. Бинарный поиск, поиск по ответу и унимодальный поиск

Этап **A1**. Core: **12**. Extra: **19**. Теория и признаки распознавания: [ROADMAP: binary search](ROADMAP.md#topic-binary-search).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 704 - Binary Search](https://leetcode.com/problems/binary-search/) | LC Easy | Классический binary search |
| 2 | `Core` | [LC 278 - First Bad Version](https://leetcode.com/problems/first-bad-version/) | LC Easy | Чистый `first true` на монотонном предикате |
| 3 | `Core` | [LC 34 - Find First and Last Position](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | LC Medium | Два граничных поиска: first `>= x` и first `> x` |
| 4 | `Core` | [CF EDU 6.1A - Binary Search](https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/A) | EDU | Наличие элемента в отсортированном массиве |
| 5 | `Core` | [CF EDU 6.1B - Closest to the Left](https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/B) | EDU | Последний элемент `<= x`, или sentinel |
| 6 | `Core` | [CF EDU 6.1C - Closest to the Right](https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/C) | EDU | Первый элемент `>= x`, или позиция за концом |
| 7 | `Core` | [CF EDU 6.1D - Fast Search](https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/D) | EDU | Две границы для числа элементов в `[l, r]` |
| 8 | `Core` | [LC 875 - Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | LC Medium | Binary search on answer и ceiling division |
| 9 | `Core` | [CF EDU 6.2A - Packing Rectangles](https://codeforces.com/edu/course/2/lesson/6/2/practice/contest/283932/problem/A) | EDU | Минимальный размер квадрата через `first true` |
| 10 | `Core` | [CF EDU 6.2C - Very Easy Task](https://codeforces.com/edu/course/2/lesson/6/2/practice/contest/283932/problem/C) | EDU | Минимальное время производства двумя машинами |
| 11 | `Core` | [CF EDU 6.2F - String Game](https://codeforces.com/edu/course/2/lesson/6/2/practice/contest/283932/problem/F) | EDU | Максимальное число удалений и subsequence-check |
| 12 | `Core` | [CF EDU 6.3B - Splitting an Array](https://codeforces.com/edu/course/2/lesson/6/3/practice/contest/285083/problem/B) | EDU | Минимизация максимальной суммы блока через greedy `can(x)` |
| 13 | `Extra` | [CF EDU 6.2B - Ropes](https://codeforces.com/edu/course/2/lesson/6/2/practice/contest/283932/problem/B) | EDU | Вещественный binary search по длине |
| 14 | `Extra` | [CF EDU 6.2D - Children Holiday](https://codeforces.com/edu/course/2/lesson/6/2/practice/contest/283932/problem/D) | EDU | Производительность с циклами отдыха и восстановление распределения |
| 15 | `Extra` | [CF EDU 6.2E - Equation](https://codeforces.com/edu/course/2/lesson/6/2/practice/contest/283932/problem/E) | EDU | Вещественный `first true` для монотонной функции |
| 16 | `Extra` | [CF EDU 6.3A - Get together](https://codeforces.com/edu/course/2/lesson/6/3/practice/contest/285083/problem/A) | EDU | Пересечение достижимых интервалов к моменту времени |
| 17 | `Extra` | [CF EDU 6.3C - Cows in Stalls](https://codeforces.com/edu/course/2/lesson/6/3/practice/contest/285083/problem/C) | EDU | Максимизация минимального расстояния через greedy placement |
| 18 | `Extra` | [CF EDU 6.3D - Minimum maximum on the Path](https://codeforces.com/edu/course/2/lesson/6/3/practice/contest/285083/problem/D) | EDU | Предикат существования пути с ограничением на ребро |
| 19 | `Extra` | [CF EDU 6.4A - Maximum Average Segment](https://codeforces.com/edu/course/2/lesson/6/4/practice/contest/285084/problem/A) | EDU | Вычитание ответа и prefix minimum для среднего |
| 20 | `Extra` | [CF EDU 6.4B - Student Councils](https://codeforces.com/edu/course/2/lesson/6/4/practice/contest/285084/problem/B) | EDU | Максимальное число групп через ограниченный вклад каждого ресурса |
| 21 | `Extra` | [CF EDU 6.4C - Pair Selection](https://codeforces.com/edu/course/2/lesson/6/4/practice/contest/285084/problem/C) | EDU | Максимальное отношение через преобразование суммы |
| 22 | `Extra` | [CF EDU 6.5A - K-th Number in the Union of Segments](https://codeforces.com/edu/course/2/lesson/6/5/practice/contest/285085/problem/A) | EDU | K-й объект через функцию количества `<= x` |
| 23 | `Extra` | [CF EDU 6.5B - Multiplication Table](https://codeforces.com/edu/course/2/lesson/6/5/practice/contest/285085/problem/B) | EDU | K-е произведение через суммарный count по строкам |
| 24 | `Extra` | [CF EDU 6.5C - K-th Sum](https://codeforces.com/edu/course/2/lesson/6/5/practice/contest/285085/problem/C) | EDU | K-я парная сумма через count и два указателя |
| 25 | `Extra` | [CF 706B - Interesting drink](https://codeforces.com/problemset/problem/706/B) | CF 1100 | Upper bound: число элементов не больше `x` |
| 26 | `Extra` | [CF 1742E - Scuza](https://codeforces.com/problemset/problem/1742/E) | CF 1200 | Upper bound по максимумам префикса плюс сумма префикса |
| 27 | `Extra` | [CF 670D1 - Magic Powder - 1](https://codeforces.com/problemset/problem/670/D1) | CF 1400 | Binary search on answer плюс линейная `can(x)` |
| 28 | `Extra` | [ACMP 523 - Роман в томах](https://acmp.ru/index.asp?main=task&id_task=523) | - | Минимизация максимального блока через greedy `can(x)` |
| 29 | `Extra` | [CF 371C - Hamburgers](https://codeforces.com/problemset/problem/371/C) | CF 1600 | Поиск ответа с аккуратной верхней границей и `long` |
| 30 | `Extra` | [CF 1355E - Restorer Distance](https://codeforces.com/problemset/problem/1355/E) | CF 2100 | Дискретная унимодальность и тернарный поиск стоимости |
| 31 | `Extra` | [LC 410 - Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) | LC Hard | Binary search по максимальной сумме + greedy count частей |

<a id="practice-greedy"></a>

## 13. Жадные алгоритмы и доказательство корректности

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

Этап **A1**. Core: **5**. Extra: **6**. Теория и признаки распознавания: [ROADMAP: биты и маски](ROADMAP.md#topic-bitmasks).

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

## Модуль 17. Базовые строковые алгоритмы

### 17.1. Префикс-функция, Z-функция и хеширование

Этап **A1**. Core: **6**. Extra: **5**. Теория и признаки распознавания: [ROADMAP: базовые строки](ROADMAP.md#topic-prefix-z-hash).

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

<a id="practice-trie"></a>

### 17.2. Trie и словарные префиксные запросы

Этап **A1**. Core: **3**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: trie](ROADMAP.md#topic-trie).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 208 - Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) | LC Medium | `insert/search/startsWith` и terminal flag |
| 2 | `Core` | Локальный checkpoint: trie на primitive arrays | Checkpoint | `next`, `terminal`, `prefixCount`, удаление через счетчики и оценка памяти |
| 3 | `Core` | [CSES - Word Combinations](https://cses.fi/problemset/task/1731) | - | Trie словаря плюс DP по позициям строки |
| 4 | `Extra` | [CF 514C - Watto and Mechanism](https://codeforces.com/problemset/problem/514/C) | CF 1700 | Trie/хеширование и ровно одно несовпадение |
| 5 | `Extra` | [CF 271D - Good Substrings](https://codeforces.com/problemset/problem/271/D) | CF 1800 | Trie различных подстрок с ограничением на плохие символы |

<a id="practice-graph-traversals"></a>

## Модуль 18. Связность графов

### 18.1. Обходы графа, компоненты, циклы и двудольность

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

<a id="practice-dsu"></a>

### 18.2. DSU: компоненты, метаданные и DSU-next

Этап **A1**. Core: **5**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: DSU](ROADMAP.md#topic-dsu).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 721 - Accounts Merge](https://leetcode.com/problems/accounts-merge/) | LC Medium | Объединение объектов по общим идентификаторам |
| 2 | `Core` | Локальный checkpoint: DSU API | Checkpoint | `find/union/same/componentSize/components` и stress против явных компонент |
| 3 | `Core` | [CF 1167C - News Distribution](https://codeforces.com/problemset/problem/1167/C) | CF 1400 | Групповые объединения и размер компоненты каждого элемента |
| 4 | `Core` | [CF 25D - Roads not only in Berland](https://codeforces.com/problemset/problem/25/D) | CF 1700 | Лишние ребра и восстановление связного дерева |
| 5 | `Core` | [CF 566D - Restructuring Company](https://codeforces.com/problemset/problem/566/D) | CF 2100 | DSU-next для пакетного объединения диапазона |
| 6 | `Extra` | [CSES - Road Construction](https://cses.fi/problemset/task/1676) | - | Online-объединения, число компонент и размер максимальной компоненты |
| 7 | `Extra` | [CF 1012B - Chemical table](https://codeforces.com/problemset/problem/1012/B) | CF 1800 | Двудольная модель компонент строк и столбцов |

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

## Модуль 21. Базовое DP и ациклические графы состояний

### 21.1. Базовое DP: пути, рюкзак, LIS и восстановление ответа

Этап **A1**. Core: **7**. Extra: **11**. Теория и признаки распознавания: [ROADMAP: базовое DP](ROADMAP.md#topic-basic-dp-core).

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
| 17 | `Extra` | [LC 509 - Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | LC Easy | Базовая линейная рекуррентность; решить итеративно, не матрицами |
| 18 | `Extra` | [CF 225C - Barcode](https://codeforces.com/problemset/problem/225/C) | CF 1700 | DP по префиксу и длине одноцветного блока |

<a id="practice-dag"></a>

### 21.2. DAG: топологическая сортировка, поиск цикла и DP

Этап **A1**. Core: **5**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: DAG](ROADMAP.md#topic-dag).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CSES - Course Schedule](https://cses.fi/problemset/task/1679) | - | Kahn, indegree и обнаружение ориентированного цикла |
| 2 | `Core` | [CF 510C - Fox And Names](https://codeforces.com/problemset/problem/510/C) | CF 1700 | Построение ограничений порядка символов и topological sort |
| 3 | `Core` | [CSES - Longest Flight Route](https://cses.fi/problemset/task/1680) | - | Максимальный путь в DAG и восстановление parent |
| 4 | `Core` | [CF 919D - Substring](https://codeforces.com/problemset/problem/919/D) | CF 1800 | DP по topological order с состоянием по символу |
| 5 | `Core` | [CSES - Game Routes](https://cses.fi/problemset/task/1681) | - | Число путей в DAG по модулю |
| 6 | `Extra` | [CF 721C - Journey](https://codeforces.com/problemset/problem/721/C) | CF 2200 | DAG DP по времени и числу вершин с восстановлением |
| 7 | `Extra` | [CF 1385E - Directing Edges](https://codeforces.com/problemset/problem/1385/E) | CF 1900 | Топологический порядок фиксированных ребер и ориентация остальных |

<a id="practice-fenwick"></a>

## 22. Fenwick tree

Этап **A1**. Core: **4**. Extra: **3**. Теория и признаки распознавания: [ROADMAP: Fenwick](ROADMAP.md#topic-fenwick).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 307 - Range Sum Query Mutable](https://leetcode.com/problems/range-sum-query-mutable/) | LC Medium | point update и range sum |
| 2 | `Core` | [ACMP 1084 - Дерево Фенвика](https://acmp.ru/index.asp?main=task&id_task=1084) | - | Базовый `add`, prefix sum и range sum |
| 3 | `Core` | [CF 652D - Nested Segments](https://codeforces.com/problemset/problem/652/D) | CF 1800 | Offline dominance: сортировка по одной границе и Fenwick по другой |
| 4 | `Core` | [CF 1208D - Restore Permutation](https://codeforces.com/problemset/problem/1208/D) | CF 1900 | Поиск позиции по взвешенной префиксной сумме спуском по Fenwick |
| 5 | `Extra` | [CF 459D - Pashmak and Parmida's problem](https://codeforces.com/problemset/problem/459/D) | CF 1800 | Преобразование элементов в частотные ранги и подсчет пар Fenwick-ом |
| 6 | `Extra` | [CF 61E - Enemy is weak](https://codeforces.com/problemset/problem/61/E) | CF 1900 | Вклад среднего элемента в убывающие тройки через два направления |
| 7 | `Extra` | [CF 220B - Little Elephant and Array](https://codeforces.com/problemset/problem/220/B) | CF 2200 | Offline-запросы по правой границе + Fenwick событий частоты |

<a id="practice-static-rmq"></a>

## 23. Static RMQ и sparse table

Этап **A1**. Core: **4**. Extra: **2**. Теория и признаки распознавания: [ROADMAP: static RMQ](ROADMAP.md#topic-static-rmq).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: sparse table | Checkpoint | Построить RMQ min и сверить все непустые диапазоны случайных массивов с наивным ответом |
| 2 | `Core` | [CF 1709D - Rorororobot](https://codeforces.com/problemset/problem/1709/D) | CF 1700 | Static range maximum плюс арифметическая достижимость |
| 3 | `Core` | [CF 1548B - Integers Have Friends](https://codeforces.com/problemset/problem/1548/B) | CF 1800 | GCD sparse table на соседних разностях и монотонный поиск границы |
| 4 | `Core` | [CF 359D - Pair of Numbers](https://codeforces.com/problemset/problem/359/D) | CF 2000 | Две static tables для `min` и `gcd`, binary search длины и восстановление всех ответов |
| 5 | `Extra` | [CF 474F - Ant Colony](https://codeforces.com/problemset/problem/474/F) | CF 2100 | GCD/min диапазона плюс частота точного значения через списки позиций |
| 6 | `Extra` | [CF 689D - Friends and Subsequences](https://codeforces.com/problemset/problem/689/D) | CF 2100 | Сравнить два решения: sparse table плюс binary searches и linear monotonic deques |

<a id="practice-segment-tree"></a>

## 24. Segment tree и lazy propagation

Этап **A1**. Core: **5**. Extra: **3**. Теория и признаки распознавания: [ROADMAP: segment tree](ROADMAP.md#topic-segment-tree).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [ACMP 1185 - RMQ с изменением элемента](https://acmp.ru/index.asp?main=task&id_task=1185) | - | Point assignment и range maximum |
| 2 | `Core` | [CF 339D - Xenia and Bit Operations](https://codeforces.com/problemset/problem/339/D) | CF 1700 | Point update и merge, зависящий от уровня дерева |
| 3 | `Core` | [CF 380C - Sereja and Brackets](https://codeforces.com/problemset/problem/380/C) | CF 2000 | Собственный ассоциативный узел для скобочной последовательности |
| 4 | `Core` | Локальный checkpoint: segment tree и lazy | Checkpoint | Range add + range min; stress-test против массива; композиция add и assign |
| 5 | `Core` | [CF 52C - Circular RMQ](https://codeforces.com/problemset/problem/52/C) | CF 2200 | `range add + range min`, lazy tags и разбиение циклического диапазона |
| 6 | `Extra` | [LC 715 - Range Module](https://leetcode.com/problems/range-module/) | LC Hard | Динамическое покрытие диапазонов и lazy propagation |
| 7 | `Extra` | [CF 242E - XOR on Segment](https://codeforces.com/problemset/problem/242/E) | CF 2000 | Побитовый составной узел и lazy range xor |
| 8 | `Extra` | [CF 438D - The Child and Sequence](https://codeforces.com/problemset/problem/438/D) | CF 2300 | Амортизированное pruning по максимуму для modulo; это не стандартный lazy |

<a id="practice-geometry"></a>

## Модуль 25. Вычислительная геометрия

<a id="practice-geometry-predicates"></a>

### 25.1. Точные геометрические предикаты и пересечения

Этап **B**. Core: **4**. Extra: **2**. Теория: [ROADMAP](ROADMAP.md#topic-geometry-predicates).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CSES - Point Location Test](https://cses.fi/problemset/task/2189) | - | Знак cross product и left/right/touch |
| 2 | `Core` | [ACMP 348 - Пересечение отрезков](https://acmp.ru/index.asp?main=task&id_task=348) | - | Orientation, point-on-segment и вырожденные пересечения |
| 3 | `Core` | [CF 772B - Volatile Kite](https://codeforces.com/problemset/problem/772/B) | CF 1800 | Расстояние от точки до прямой через cross product |
| 4 | `Core` | Локальный checkpoint: Geometry primitives | Checkpoint | Dot/cross, projection, distance to segment и stress пересечений на целых координатах |
| 5 | `Extra` | [LC 149 - Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/) | LC Hard | Нормализация направления через gcd и группы коллинеарных точек |
| 6 | `Extra` | [CF 13B - Letter A](https://codeforces.com/problemset/problem/13/B) | CF 1900 | Пересечения и геометрические ограничения составной фигуры |

<a id="practice-polygons"></a>

### 25.2. Простые многоугольники: площадь и point-in-polygon

Этап **B**. Core: **3**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-polygons).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [ACMP 370 - Площадь многоугольника](https://acmp.ru/index.asp?main=task&id_task=370) | - | Shoelace и удвоенная ориентированная площадь |
| 2 | `Core` | [CSES - Point in Polygon](https://cses.fi/problemset/task/2192) | - | Boundary check плюс ray casting с корректными вершинами |
| 3 | `Core` | Локальный checkpoint: polygon API | Checkpoint | Area, boundary, inside/outside на выпуклых и невыпуклых многоугольниках |
| 4 | `Extra` | [CF 993A - Two Squares](https://codeforces.com/problemset/problem/993/A) | CF 1600 | Пересечения сторон и containment выпуклых фигур |

<a id="practice-convex-hull"></a>

### 25.3. Выпуклая оболочка и запросы на ней

Этап **B**. Core: **3**. Extra: **2**. Теория: [ROADMAP](ROADMAP.md#topic-convex-hull).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [ACMP 374 - Выпуклая оболочка - 2](https://acmp.ru/index.asp?main=task&id_task=374) | - | Monotone chain и политика коллинеарных точек |
| 2 | `Core` | [CSES - Convex Hull](https://cses.fi/problemset/task/2195) | - | Полная `O(n log n)` оболочка с граничными точками |
| 3 | `Core` | [CF 166B - Polygons](https://codeforces.com/problemset/problem/166/B) | CF 2100 | Строгий point-in-convex за `O(log n)` без касаний |
| 4 | `Extra` | [CF 70D - Professor's task](https://codeforces.com/problemset/problem/70/D) | CF 2600 | Динамическая выпуклая оболочка и point location |
| 5 | `Extra` | [CSES - Line Segment Intersection](https://cses.fi/problemset/task/2190) | - | Повтор точных предикатов перед продвинутой оболочкой |

<a id="practice-rotating-calipers"></a>

### 25.4. Вращающиеся калиперы

Этап **C**. Core: **2**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-rotating-calipers).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: diameter of convex polygon | Checkpoint | Оболочка уже дана; два циклических указателя и сравнение squared distance |
| 2 | `Core` | [CF Gym 101554D - Robert Hood](https://codeforces.com/gym/101554/problem/D) | - | Convex hull плюс rotating calipers для диаметра множества |
| 3 | `Extra` | [Kattis - roberthood](https://open.kattis.com/problems/roberthood) | - | Независимая повторная проверка diameter pipeline |

<a id="practice-geometry-sweep"></a>

### 25.5. Геометрический sweep

Этап **C**. Core: **2**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-geometry-sweep).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CSES - Intersection Points](https://cses.fi/problemset/task/1740) | - | Sweep горизонтальных/вертикальных отрезков плюс Fenwick |
| 2 | `Core` | Локальный checkpoint: segment events | Checkpoint | Start/query/end tie-break и active ordered structure на малых тестах |
| 3 | `Extra` | [CF 19D - Points](https://codeforces.com/problemset/problem/19/D) | CF 2500 | Динамические точки, coordinate compression и ordered range search |

<a id="practice-closest-pair"></a>

### 25.6. Пара ближайших точек

Этап **C**. Core: **2**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-closest-pair).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CSES - Minimum Euclidean Distance](https://cses.fi/problemset/task/2194) | - | Closest pair divide-and-conquer за `O(n log n)` |
| 2 | `Core` | Локальный checkpoint: closest pair | Checkpoint | Сохранение sort-by-y, strip и stress против `O(n^2)` |
| 3 | `Extra` | [Kattis - closestpair1](https://open.kattis.com/problems/closestpair1) | - | Восстановление самой пары и floating-point output |

<a id="practice-advanced-graphs"></a>

## Модуль 26. Структура графов

<a id="practice-scc"></a>

### 26.1. SCC и граф конденсации

Этап **B**. Core: **3**. Extra: **2**. Теория: [ROADMAP](ROADMAP.md#topic-scc).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CSES - Planets and Kingdoms](https://cses.fi/problemset/task/1683) | - | Kosaraju/Tarjan и номер SCC каждой вершины |
| 2 | `Core` | [CF 427C - Checkposts](https://codeforces.com/problemset/problem/427/C) | CF 1700 | SCC плюс минимум и число способов внутри компоненты |
| 3 | `Core` | [CSES - Coin Collector](https://cses.fi/problemset/task/1686) | - | Condensation DAG и DP максимальной суммы |
| 4 | `Extra` | [CF 999E - Reachability from the Capital](https://codeforces.com/problemset/problem/999/E) | CF 1800 | Истоки недостижимой части condensation |
| 5 | `Extra` | [CF 1239D - Catowice City](https://codeforces.com/problemset/problem/1239/D) | CF 2200 | SCC-подобное разбиение ориентированных отношений |

<a id="practice-two-sat"></a>

### 26.2. 2-SAT

Этап **B**. Core: **2**. Extra: **2**. Теория: [ROADMAP](ROADMAP.md#topic-two-sat).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CSES - Giant Pizza](https://cses.fi/problemset/task/1684) | - | Clauses, implication graph и восстановление assignment |
| 2 | `Core` | [CF 776D - The Door Problem](https://codeforces.com/problemset/problem/776/D) | CF 2200 | Равенство/неравенство двух булевых переменных как 2-SAT |
| 3 | `Extra` | [CF 468B - Two Sets](https://codeforces.com/problemset/problem/468/B) | CF 2100 | Выбор группы и импликации по необходимым дополнениям |
| 4 | `Extra` | [CF 27D - Ring Road 2](https://codeforces.com/problemset/problem/27/D) | CF 2400 | Геометрические конфликты хорд как булевы ограничения |

<a id="practice-bridges-biconnected"></a>

### 26.3. Мосты, точки сочленения и компоненты двусвязности

Этап **B**. Core: **4**. Extra: **3**. Теория: [ROADMAP](ROADMAP.md#topic-bridges-biconnected).

| № | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 1192 - Critical Connections](https://leetcode.com/problems/critical-connections-in-a-network/) | LC Hard | Мосты через `tin/low` |
| 2 | `Core` | [CF Gym 100083D - Точки сочленения](https://codeforces.com/gym/100083/problem/D) | - | Root case и articulation points |
| 3 | `Core` | [CSES - Necessary Roads](https://cses.fi/problemset/task/2076) | - | Multigraph-safe поиск всех мостов по edge id |
| 4 | `Core` | [CF 1000E - We Need More Bosses](https://codeforces.com/problemset/problem/1000/E) | CF 2100 | 2-edge-connected components, bridge tree и диаметр |
| 5 | `Extra` | [CF 118E - Bertown roads](https://codeforces.com/problemset/problem/118/E) | CF 2000 | Отсутствие мостов и сильная ориентация ребер |
| 6 | `Extra` | [CF 652E - Pursuit For Artifacts](https://codeforces.com/problemset/problem/652/E) | CF 2300 | Bridge tree и агрегат на пути |
| 7 | `Extra` | [CF 732F - Tourist Reform](https://codeforces.com/problemset/problem/732/F) | CF 2400 | Мосты, 2-edge-components и ориентация для максимальной SCC |

<a id="practice-dsu-mst"></a>

## Модуль 27. Остовы и монотонная связность

<a id="practice-mst"></a>

### 27.1. Минимальные остовы

Этап **B**. Core: **4**. Extra: **2**. Теория: [ROADMAP](ROADMAP.md#topic-mst).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 1584 - Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | LC Medium | Dense Prim и полный граф расстояний |
| 2 | `Core` | [ACMP 142 - Минимальный каркас](https://acmp.ru/index.asp?main=task&id_task=142) | - | Базовый Kruskal + DSU |
| 3 | `Core` | Локальный checkpoint: sparse Prim | - | Heap, visited и disconnected graph |
| 4 | `Core` | [CF 1245D - Shichikuji and Power Grid](https://codeforces.com/problemset/problem/1245/D) | CF 1900 | Virtual source, Prim и восстановление сети |
| 5 | `Extra` | [CF 160D - Edges in MST](https://codeforces.com/problemset/problem/160/D) | CF 2300 | Группы равных весов и классификация ребер MST |
| 6 | `Extra` | [CF 609E - Minimum spanning tree for each edge](https://codeforces.com/problemset/problem/609/E) | CF 2100 | MST + maximum edge on path |

<a id="practice-dsu-offline-activation"></a>

### 27.2. Офлайн-активация через DSU

Этап **B**. Core: **3**. Extra: **2**. Теория: [ROADMAP](ROADMAP.md#topic-dsu-offline-activation).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: component size under threshold | - | Сортировка ребер и запросов с одинаковым порогом |
| 2 | `Core` | [CF 1213G - Path Queries](https://codeforces.com/problemset/problem/1213/G) | CF 1800 | Активация ребер по весу + metadata компонент |
| 3 | `Core` | [CF 722C - Destroying Array](https://codeforces.com/problemset/problem/722/C) | CF 1900 | Обратное время: удаления превращаются в добавления |
| 4 | `Extra` | [CF 1513D - GCD and MST](https://codeforces.com/problemset/problem/1513/D) | CF 1800 | Монотонная активация дешевых связей |
| 5 | `Extra` | [CF 1706E - Qpwoeirut And Vertices](https://codeforces.com/problemset/problem/1706/E) | CF 2100 | Kruskal reconstruction tree после монотонных union |

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

Этап **B**. Core: **2**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-layered-grid-dp).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 1695C - Zero Path](https://codeforces.com/problemset/problem/1695/C) | CF 1700 | Min/max достижимой суммы, длина и четность пути |
| 2 | `Core` | [CF 1517D - Explorer Space](https://codeforces.com/problemset/problem/1517/D) | CF 1800 | DP на точное число шагов и rolling layers |
| 3 | `Extra` | [CF 118D - Caesar's Legions](https://codeforces.com/problemset/problem/118/D) | CF 1800 | Состояние по позиции, последнему типу и длине серии |

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
| 2 | `Core` | [CSES - All Palindromes](https://cses.fi/problemset/task/2420) | - | Вывод всех длин из массивов радиусов |
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

### 33.3. Small-to-large и DSU on tree

Этап **B**. Core: **3**. Extra: **2**. Теория: [ROADMAP](ROADMAP.md#topic-small-to-large).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CSES - Distinct Colors](https://cses.fi/problemset/task/1139) | - | Merge smaller color set into larger |
| 2 | `Core` | Локальный checkpoint: frequency maps in every subtree | - | Амортизация перемещений элементов |
| 3 | `Core` | [CF 600E - Lomsat gelral](https://codeforces.com/problemset/problem/600/E) | CF 2300 | DSU on tree и агрегат цветов максимальной частоты |
| 4 | `Extra` | [CF 375D - Tree and Queries](https://codeforces.com/problemset/problem/375/D) | CF 2300 | Частоты частот в поддеревьях |
| 5 | `Extra` | [CF 570D - Tree Requests](https://codeforces.com/problemset/problem/570/D) | CF 2200 | Depth buckets и parity masks; сравнить с offline Euler |

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

### 36.1. Sqrt decomposition по блокам

Этап **C**. Core: **3**. Extra: **3**. Теория: [ROADMAP](ROADMAP.md#topic-sqrt-blocks).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: point update + range sum | - | Полные и краевые блоки |
| 2 | `Core` | Локальный checkpoint: range add + range sum | - | Lazy tag и агрегат блока |
| 3 | `Core` | Локальный checkpoint: count values below x | - | Sorted blocks и пересборка после update |
| 4 | `Extra` | [CF 13E - Holes](https://codeforces.com/problemset/problem/13/E) | CF 2200 | Jump pointers внутри блоков |
| 5 | `Extra` | [CF 455D - Serega and Fun](https://codeforces.com/problemset/problem/455/D) | CF 2600 | Динамические блоки последовательности |
| 6 | `Extra` | [CF 1207F - Remainder Problem](https://codeforces.com/problemset/problem/1207/F) | CF 2100 | Разделение запросов по малому/большому модулю |

<a id="practice-mo"></a>

### 36.2. Алгоритм Мо

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

Этап **C**. Core: **3**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-persistence).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [LC 1146 - Snapshot Array](https://leetcode.com/problems/snapshot-array/) | LC Medium | Вводная версия значений по времени |
| 2 | `Core` | [CSES - Range Queries and Copies](https://cses.fi/problemset/task/1737) | - | Path-copying segment tree и roots версий |
| 3 | `Core` | [CF 813E - Army Creation](https://codeforces.com/problemset/problem/813/E) | CF 2200 | Persistent segment tree по префиксам |
| 4 | `Extra` | [CF 484E - Sign on Fence](https://codeforces.com/problemset/problem/484/E) | CF 2600 | Версии по порогу + binary search answer |

<a id="practice-dynamic-connectivity"></a>

### 37.3. Rollback DSU и offline dynamic connectivity

Этап **C**. Core: **3**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-dynamic-connectivity).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: RollbackDSU | - | Union by size без path compression, snapshot и undo |
| 2 | `Core` | [CSES - Dynamic Connectivity](https://cses.fi/problemset/task/2133) | - | Интервалы жизни ребер + segment tree over time |
| 3 | `Core` | [CF 891C - Envy](https://codeforces.com/problemset/problem/891/C) | CF 2600 | Временные union групп запросов и rollback |
| 4 | `Extra` | [CF 1140F - Extending Set of Points](https://codeforces.com/problemset/problem/1140/F) | CF 2700 | Dynamic bipartite components и rollback metadata |

<a id="practice-dp-optimizations"></a>

## Модуль 38. Оптимизации DP

<a id="practice-monotone-cht"></a>

### 38.1. Monotone CHT

Этап **B**. Core: **1**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-monotone-cht).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 319C - Kalila and Dimna in the Logging Industry](https://codeforces.com/problemset/problem/319/C) | CF 2100 | Монотонные slopes и query coordinates |
| 2 | `Extra` | [CF 660F - Bear and Bowling 4](https://codeforces.com/problemset/problem/660/F) | CF 2400 | Монотонные slopes, произвольные `x`, hull + binary search; не Li Chao |

<a id="practice-li-chao"></a>

### 38.2. Li Chao Tree

Этап **C**. Core: **1**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-li-chao).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CSES - Monster Game II](https://cses.fi/problemset/task/2085) | - | Произвольные slopes и `x`, online add/query |
| 2 | `Extra` | [CF 932F - Escape Through Leaf](https://codeforces.com/problemset/problem/932/F) | CF 2600 | Tree DP + small-to-large line containers |

<a id="practice-divide-conquer-dp"></a>

### 38.3. Divide-and-conquer optimization DP

Этап **C**. Core: **1**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-divide-conquer-dp).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 321E - Ciel and Gondolas](https://codeforces.com/problemset/problem/321/E) | CF 2600 | Monotone opt и `O(1)` cost через 2D prefix sums |
| 2 | `Extra` | [CF 868F - Yet Another Minimization Problem](https://codeforces.com/problemset/problem/868/F) | CF 2500 | D&C optimization + подвижная стоимость окна |

<a id="practice-knuth"></a>

### 38.4. Оптимизация Кнута

Этап **C**. Core: **1**. Extra: **1**. Теория: [ROADMAP](ROADMAP.md#topic-knuth).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CSES - Knuth Division](https://cses.fi/problemset/task/2088) | - | Каноническое interval DP и границы opt |
| 2 | `Extra` | [CF Gym 100212C - Order-Preserving Codes](https://codeforces.com/gym/100212/problem/C) | - | Knuth + моделирование и восстановление кодов |

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

Этап **C**. Core: **3**. Extra: **2**. Теория: [ROADMAP](ROADMAP.md#topic-convolution).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | Локальный checkpoint: naive convolution + NTT stress | - | Padding, inverse и сравнение с `O(nm)` |
| 2 | `Core` | [CSES - Apples and Bananas](https://cses.fi/problemset/task/2111) | - | Частоты парных сумм как convolution |
| 3 | `Core` | [Library Checker - Convolution Mod](https://judge.yosupo.jp/problem/convolution_mod) | - | Самостоятельная NTT modulo `998244353` |
| 4 | `Extra` | [CF 1096G - Lucky Tickets](https://codeforces.com/problemset/problem/1096/G) | CF 2300 | Generating function и быстрое возведение полинома |
| 5 | `Extra` | [CF 528D - Fuzzy Search](https://codeforces.com/problemset/problem/528/D) | CF 2500 | Корреляция строк через несколько сверток |

<a id="practice-probability-interactive"></a>

## Модуль 40. Вероятность, рандомизация и специальные форматы

<a id="practice-probability"></a>

### 40.1. Вероятность и математическое ожидание

Этап **B**. Core: **5**. Теория: [ROADMAP](ROADMAP.md#topic-probability).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [CF 453A - Little Pony and Expected Maximum](https://codeforces.com/problemset/problem/453/A) | CF 1600 | CDF максимума и tail-sum expectation |
| 2 | `Core` | [CF 839C - Journey](https://codeforces.com/problemset/problem/839/C) | CF 1600 | Условное ожидание по дереву |
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
| 2 | `Extra` | [CF 1114E - Arithmetic Progression](https://codeforces.com/problemset/problem/1114/E) | CF 2400 | Interactive + binary search + randomized sampling |

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

Этап **C**. Core: **2**. Теория: [ROADMAP](ROADMAP.md#topic-scored-constructive).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [МОШ 2025/26, задача B1](contests/14-moscow/2025-2026/final/full-with-answers-checkers.zip) | - | Сначала valid output программы, затем улучшение score |
| 2 | `Core` | [МОШ 2025/26, задача B2](contests/14-moscow/2025-2026/final/full-with-answers-checkers.zip) | - | Локальный checker и итеративная constructive heuristic |

<a id="practice-open-test-batch"></a>

### 40.7. Open-test Batch

Этап **C**. Core: **1**. Теория: [ROADMAP](ROADMAP.md#topic-open-test-batch).

| N | Приоритет | Задача | Сложность | Паттерн |
| --: | :---: | --- | --- | --- |
| 1 | `Core` | [СПбГУ 2024/25, задача B](contests/03-spbu/2024-2025/final-statements.pdf) | - | Открытые inputs, но submission остается программой |
