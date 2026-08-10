# Прогресс подготовки

Исходный уровень выставляется только по фактически пройденным Core и решениям в смешанных контестах. Карта показывает
подтвержденную практикой готовность по каждой теме.

## Уровни освоения

| Уровень | Что означает      | Проверяемое основание                                                                    |
| ------: | ----------------- | ---------------------------------------------------------------------------------------- |
|     `0` | Не проверено      | По теме еще не было практики                                                             |
|     `1` | Знакомится        | Понимает признаки и прошел первые Core с материалом, подсказкой или последующим upsolve |
|     `2` | Умеет применять   | Завершил все Core темы, включая checkpoints, и пишет базовую реализацию на Java          |
|     `3` | Готов к олимпиаде | После Core самостоятельно решил новую или смешанную задачу в установленное время         |
|     `4` | Навык закреплен   | Через 7-14 дней снова применил тему в новой задаче или смешанном контесте                 |

Просмотр теории или разбора сам по себе уровень не повышает. Одна неудачная задача тоже не понижает его автоматически: для понижения нужны две независимые проверки, показавшие одну и ту же проблему.

Колонка `Паттерн` в [`PRACTICE.md`](PRACTICE.md) видна как учебная карта. Для независимой проверки ученик сначала
открывает только условие и не читает эту колонку. Решение после подсказки засчитывается в прохождение Core и уровень
`2`, но уровень `3` подтверждается новой или смешанной задачей без раскрытого паттерна.

Уровень `3` сам по себе образует очередь повторения. Каждую неделю из таких тем выбираются 2-3 темы: сначала
приоритеты `A0/A1`, затем темы, которые дольше не встречались в практике. Отдельный календарь повторений вести не
нужно.

## Карта тем

| ID | Тема | Приоритет | Уровень `0-4` |
| ---: | --- | :---: | :---: |
| 1 | [Оценка сложности, Java и аккуратная реализация](ROADMAP.md#topic-complexity-java) | A0 | 0 |
| 2.1 | [Полный перебор пространства вариантов](ROADMAP.md#topic-bruteforce-enumeration) | A0 | 0 |
| 2.2 | [Backtracking, rollback и безопасные отсечения](ROADMAP.md#topic-backtracking) | A0 | 0 |
| 3.1 | [Сравнительная сортировка, компараторы и восстановление порядка](ROADMAP.md#topic-sorting-comparators) | A0 | 0 |
| 3.2 | [Counting sort и radix sort](ROADMAP.md#topic-integer-sorting) | A0 | 0 |
| 3.3 | [Сжатие координат](ROADMAP.md#topic-coordinate-compression) | A0 | 0 |
| 4.1 | [Частоты, HashMap, HashSet и канонические ключи](ROADMAP.md#topic-hash-containers) | A0 | 0 |
| 4.2 | [Ordered set, multiset и поиск соседнего ключа](ROADMAP.md#topic-ordered-set) | A0 | 0 |
| 5.1 | [Стек: вложенность и потоковая редукция](ROADMAP.md#topic-stack) | A0 | 0 |
| 5.2 | [FIFO-очередь](ROADMAP.md#topic-queue) | A0 | 0 |
| 5.3 | [Обычный deque и lazy deletion с концов](ROADMAP.md#topic-deque) | A0 | 0 |
| 6.1 | [Динамический экстремум, best-first processing и scheduling](ROADMAP.md#topic-priority-queue-extremum) | A0 | 0 |
| 6.2 | [Bounded heap, top-k и remove-worst](ROADMAP.md#topic-bounded-heap) | A0 | 0 |
| 6.3 | [Несколько порядков доступа и stale entries](ROADMAP.md#topic-priority-queue-stale) | A0 | 0 |
| 7.1 | [Одномерные префиксные агрегаты](ROADMAP.md#topic-prefix-1d) | A1 | 0 |
| 7.2 | [Многомерные префиксы](ROADMAP.md#topic-prefix-multidimensional) | A1 | 0 |
| 7.3 | [Массив разностей и офлайн-обновления диапазонов](ROADMAP.md#topic-difference-array) | A1 | 0 |
| 7.4 | [Разности для арифметической прогрессии](ROADMAP.md#topic-difference-arithmetic-progression) | A1 | 0 |
| 7.5 | [Двумерный массив разностей](ROADMAP.md#topic-difference-2d) | A1 | 0 |
| 8.1 | [Встречные указатели в отсортированном массиве](ROADMAP.md#topic-two-pointers-opposite) | A1 | 0 |
| 8.2 | [Merge-like проход по двум последовательностям](ROADMAP.md#topic-two-pointers-merge) | A1 | 0 |
| 8.3 | [Синхронизация накопленных величин](ROADMAP.md#topic-two-pointers-synchronized) | A1 | 0 |
| 9.1 | [Фиксированное скользящее окно](ROADMAP.md#topic-fixed-window) | A1 | 0 |
| 9.2 | [Переменное sliding window](ROADMAP.md#topic-sliding-window) | A1 | 0 |
| 9.3 | [Монотонный deque для экстремума окна](ROADMAP.md#topic-monotonic-deque) | A1 | 0 |
| 9.4 | [Очередь с агрегатом на двух стеках](ROADMAP.md#topic-aggregate-queue) | B | 0 |
| 10.1 | [Ближайший меньший или больший элемент](ROADMAP.md#topic-nearest-element-stack) | A1 | 0 |
| 10.2 | [Span и максимальный прямоугольник в гистограмме](ROADMAP.md#topic-histogram-stack) | A1 | 0 |
| 10.3 | [Подсчет вкладов через монотонный стек](ROADMAP.md#topic-contribution-stack) | A1 | 0 |
| 10.4 | [Жадное удаление стеком](ROADMAP.md#topic-greedy-stack) | A1 | 0 |
| 10.5 | [DP и реконструкция поверх монотонного стека](ROADMAP.md#topic-stack-dp) | B | 0 |
| 11.1 | [Sweep line по событиям](ROADMAP.md#topic-sweep-events) | A1 | 0 |
| 11.2 | [Sweep line с active set](ROADMAP.md#topic-sweep-active-set) | A1/B | 0 |
| 12.1 | [Границы в отсортированном массиве](ROADMAP.md#topic-binary-boundaries) | A1 | 0 |
| 12.2 | [Целочисленный бинарный поиск по ответу](ROADMAP.md#topic-binary-answer-integer) | A1 | 0 |
| 12.3 | [Вещественный бинарный поиск](ROADMAP.md#topic-binary-answer-real) | A1 | 0 |
| 12.4 | [Minimax и maximin через feasibility](ROADMAP.md#topic-binary-minimax) | A1 | 0 |
| 12.5 | [Параметрический поиск среднего или отношения](ROADMAP.md#topic-parametric-average) | B | 0 |
| 12.6 | [K-й объект через функцию подсчета](ROADMAP.md#topic-binary-kth) | B | 0 |
| 12.7 | [Поиск экстремума унимодальной функции](ROADMAP.md#topic-unimodal-search) | B | 0 |
| 13.1 | [Интервальный greedy](ROADMAP.md#topic-greedy-intervals) | A1 | 0 |
| 13.2 | [Независимый локальный выбор](ROADMAP.md#topic-greedy-local) | A1 | 0 |
| 13.3 | [Greedy packing и минимальный достаточный ресурс](ROADMAP.md#topic-greedy-packing) | A1 | 0 |
| 13.4 | [Greedy frontier и поддержание достижимой границы](ROADMAP.md#topic-greedy-frontier) | A1 | 0 |
| 13.5 | [Scheduling с remove-worst](ROADMAP.md#topic-greedy-scheduling) | A1/B | 0 |
| 14.1 | [Побитовые операции и двоичное представление](ROADMAP.md#topic-bit-operations) | A1 | 0 |
| 14.2 | [Маска как компактное множество](ROADMAP.md#topic-bitmask-set) | A1 | 0 |
| 14.3 | [Перебор масок и подмасок](ROADMAP.md#topic-submask-enumeration) | A1 | 0 |
| 14.4 | [Булева алгебра и побитовые ограничения](ROADMAP.md#topic-boolean-algebra) | A1 | 0 |
| 15.1 | [GCD, LCM и делимость](ROADMAP.md#topic-gcd-lcm) | A1 | 0 |
| 15.2 | [Расширенный Евклид и линейные диофантовы уравнения](ROADMAP.md#topic-extended-euclid) | A1 | 0 |
| 15.3 | [Решето, факторизация, делители и phi](ROADMAP.md#topic-sieve-factorization) | A1 | 0 |
| 15.4 | [Линейные сравнения и generalized CRT](ROADMAP.md#topic-congruences-crt) | A1/B | 0 |
| 16.1 | [Модульная арифметика](ROADMAP.md#topic-modular-arithmetic) | A1 | 0 |
| 16.2 | [Базовая комбинаторика и биномиальные коэффициенты](ROADMAP.md#topic-combinatorics) | A1 | 0 |
| 16.3 | [Включения-исключения](ROADMAP.md#topic-inclusion-exclusion) | A1 | 0 |
| 16.4 | [Принцип Дирихле](ROADMAP.md#topic-pigeonhole-counting) | A1 | 0 |
| 17.1 | [Префикс-функция, KMP, границы и периоды](ROADMAP.md#topic-prefix-kmp) | A1 | 0 |
| 17.2 | [Z-функция и префиксные совпадения](ROADMAP.md#topic-z-function) | A1 | 0 |
| 17.3 | [Полиномиальный rolling hash подстрок](ROADMAP.md#topic-rolling-hash) | A1 | 0 |
| 17.4 | [Trie и словарные префиксные запросы](ROADMAP.md#topic-trie) | A1 | 0 |
| 18.1 | [Модель графа и представление в памяти](ROADMAP.md#topic-graph-representation) | A1 | 0 |
| 18.2 | [DFS/BFS: достижимость, компоненты и flood fill](ROADMAP.md#topic-graph-traversals) | A1 | 0 |
| 18.3 | [Циклы в ориентированном и неориентированном графе](ROADMAP.md#topic-graph-cycles) | A1 | 0 |
| 18.4 | [Двудольность и раскраска в два цвета](ROADMAP.md#topic-bipartite) | A1 | 0 |
| 18.5 | [DSU: объединение компонент и метаданные корня](ROADMAP.md#topic-dsu) | A1 | 0 |
| 18.6 | [Successor DSU и пропуск обработанных позиций](ROADMAP.md#topic-dsu-next) | A1 | 0 |
| 19.1 | [BFS shortest path и multi-source BFS](ROADMAP.md#topic-bfs-shortest) | A1 | 0 |
| 19.2 | [0-1 BFS](ROADMAP.md#topic-zero-one-bfs) | A1 | 0 |
| 19.3 | [Dijkstra для неотрицательных весов](ROADMAP.md#topic-dijkstra) | A1 | 0 |
| 19.4 | [Bellman-Ford, ограничение числа ребер и отрицательный цикл](ROADMAP.md#topic-bellman-ford) | A1 | 0 |
| 19.5 | [Floyd-Warshall и кратчайшие пути между всеми парами](ROADMAP.md#topic-floyd-warshall) | A1 | 0 |
| 20.1 | [Корневое дерево, parent/depth, поддерево и диаметр](ROADMAP.md#topic-rooted-trees) | A1 | 0 |
| 20.2 | [Euler tin/tout и поддерево как отрезок](ROADMAP.md#topic-euler-tour) | A1 | 0 |
| 20.3 | [Binary lifting, k-й предок, LCA и расстояние](ROADMAP.md#topic-lca) | A1 | 0 |
| 20.4 | [Difference-on-tree для массовых добавлений](ROADMAP.md#topic-tree-differences) | B | 0 |
| 21.1 | [Проектирование DP-состояния: линейные, сеточные и малые состояния](ROADMAP.md#topic-basic-dp-state) | A1 | 0 |
| 21.2 | [Knapsack и subset-sum по сумме/весу](ROADMAP.md#topic-knapsack) | A1 | 0 |
| 21.3 | [DP двух последовательностей: LCS и edit distance](ROADMAP.md#topic-sequence-dp) | A1 | 0 |
| 21.4 | [LIS, DP по подпоследовательности и восстановление](ROADMAP.md#topic-lis) | A1 | 0 |
| 21.5 | [Topological sort и цикл в ориентированном графе](ROADMAP.md#topic-topological-sort) | A1 | 0 |
| 21.6 | [DP и релаксации по DAG](ROADMAP.md#topic-dag-dp) | A1 | 0 |
| 22.1 | [Базовый Fenwick: изменяемые префиксные суммы](ROADMAP.md#topic-fenwick-basic) | A1 | 0 |
| 22.2 | [Offline counting и dominance через Fenwick](ROADMAP.md#topic-fenwick-offline) | A1 | 0 |
| 22.3 | [Prefix lower bound и порядковые статистики в Fenwick](ROADMAP.md#topic-fenwick-order-statistics) | A1 | 0 |
| 23 | [Static RMQ и sparse table](ROADMAP.md#topic-static-rmq) | A1 | 0 |
| 24.1 | [Segment tree как monoid и собственный узел](ROADMAP.md#topic-segment-tree-monoid) | A1/B | 0 |
| 24.2 | [Спуск по segment tree и поиск позиции](ROADMAP.md#topic-segment-tree-descent) | A1/B | 0 |
| 24.3 | [Массовое обновление и точечный запрос](ROADMAP.md#topic-range-update-point-query) | A1/B | 0 |
| 24.4 | [Lazy propagation для обновлений и запросов на отрезке](ROADMAP.md#topic-lazy-segment-tree) | A1/B | 0 |
| 24.5 | [Амортизированный pruning и граница Segment Tree Beats](ROADMAP.md#topic-segment-tree-pruning) | C | 0 |
| 25.1 | [Точные геометрические предикаты и пересечения](ROADMAP.md#topic-geometry-predicates) | B | 0 |
| 25.2 | [Простые многоугольники: площадь и point-in-polygon](ROADMAP.md#topic-polygons) | B | 0 |
| 25.3 | [Выпуклая оболочка и запросы на выпуклом многоугольнике](ROADMAP.md#topic-convex-hull) | B | 0 |
| 25.4 | [Вращающиеся калиперы](ROADMAP.md#topic-rotating-calipers) | C | 0 |
| 25.5 | [Геометрический sweep по множеству объектов](ROADMAP.md#topic-geometry-sweep) | C | 0 |
| 25.6 | [Пара ближайших точек](ROADMAP.md#topic-closest-pair) | C | 0 |
| 26.1 | [SCC и граф конденсации](ROADMAP.md#topic-scc) | B | 0 |
| 26.2 | [2-SAT: граф импликаций и SCC](ROADMAP.md#topic-two-sat) | B | 0 |
| 26.3 | [Мосты, компоненты реберной двусвязности и bridge tree](ROADMAP.md#topic-bridges-edge-bcc) | B | 0 |
| 26.4 | [Точки сочленения, вершинные блоки и block-cut tree](ROADMAP.md#topic-articulation-vertex-bcc) | B | 0 |
| 27.1 | [Минимальные остовы: cut/cycle properties, Kruskal и Prim](ROADMAP.md#topic-mst) | B | 0 |
| 27.2 | [Офлайн-активация и монотонная связность через DSU](ROADMAP.md#topic-dsu-offline-activation) | B | 0 |
| 28.1 | [DP по отрезкам](ROADMAP.md#topic-interval-dp) | B | 0 |
| 28.2 | [Слоистое DP по решетке и состояниям](ROADMAP.md#topic-layered-grid-dp) | B | 0 |
| 28.3 | [DP по поддеревьям](ROADMAP.md#topic-subtree-dp) | B | 0 |
| 28.4 | [Rerooting DP: ответы для всех корней](ROADMAP.md#topic-rerooting) | B | 0 |
| 29.1 | [DP по подмножествам](ROADMAP.md#topic-subset-dp-core) | B | 0 |
| 29.2 | [Digit DP](ROADMAP.md#topic-digit-dp) | B | 0 |
| 29.3 | [Profile DP](ROADMAP.md#topic-profile-dp) | B | 0 |
| 29.4 | [SOS DP и преобразования по подмаскам](ROADMAP.md#topic-sos-dp) | C | 0 |
| 30.1 | [Статическое декартово дерево](ROADMAP.md#topic-cartesian-tree) | B | 0 |
| 30.2 | [Explicit-key treap: динамическое упорядоченное множество](ROADMAP.md#topic-explicit-treap) | B | 0 |
| 30.3 | [Implicit treap: последовательность через split/merge](ROADMAP.md#topic-implicit-treap) | B | 0 |
| 30.4 | [Bitwise trie для XOR-запросов](ROADMAP.md#topic-bitwise-trie) | B | 0 |
| 31.1 | [Двудольное паросочетание](ROADMAP.md#topic-bipartite-matching) | B | 0 |
| 31.2 | [Максимальный поток и минимальный разрез](ROADMAP.md#topic-max-flow) | B | 0 |
| 31.3 | [Поток минимальной стоимости](ROADMAP.md#topic-min-cost-flow) | C | 0 |
| 32.1 | [Ахо-Корасик](ROADMAP.md#topic-aho-corasick) | B | 0 |
| 32.2 | [Алгоритм Манакера](ROADMAP.md#topic-manacher) | B | 0 |
| 32.3 | [Suffix array и LCP](ROADMAP.md#topic-suffix-array) | B | 0 |
| 32.4 | [Суффиксный автомат](ROADMAP.md#topic-suffix-automaton) | C | 0 |
| 33.1 | [Heavy-light decomposition](ROADMAP.md#topic-hld) | B | 0 |
| 33.2 | [Центроидная декомпозиция](ROADMAP.md#topic-centroid-decomposition) | B | 0 |
| 33.3 | [Small-to-large: слияние контейнеров поддеревьев](ROADMAP.md#topic-small-to-large) | B | 0 |
| 33.4 | [DSU on tree: keep/clear тяжелого сына](ROADMAP.md#topic-dsu-on-tree) | B | 0 |
| 34.1 | [Конечные игры и P/N-позиции](ROADMAP.md#topic-pn-games) | B | 0 |
| 34.2 | [Minimax и memoization по состояниям](ROADMAP.md#topic-minimax) | B | 0 |
| 34.3 | [Nim и теорема Шпрага-Гранди](ROADMAP.md#topic-nim-sg) | B | 0 |
| 34.4 | [Retrograde analysis игр с циклами](ROADMAP.md#topic-cyclic-games) | C | 0 |
| 35 | [Meet-in-the-middle](ROADMAP.md#topic-meet-in-the-middle) | B | 0 |
| 36.1 | [Sqrt decomposition: обычные блоки диапазонов](ROADMAP.md#topic-sqrt-blocks) | C | 0 |
| 36.2 | [Sqrt decomposition: прыжки и пересборка блока](ROADMAP.md#topic-sqrt-jump) | C | 0 |
| 36.3 | [Динамические блоки последовательности](ROADMAP.md#topic-dynamic-blocks) | C | 0 |
| 36.4 | [Разделение параметра на малый и большой](ROADMAP.md#topic-small-large-heuristics) | C | 0 |
| 36.5 | [Алгоритм Мо](ROADMAP.md#topic-mo) | C | 0 |
| 37.1 | [Rollback по дереву версий](ROADMAP.md#topic-version-rollback) | C | 0 |
| 37.2 | [Персистентные структуры и path copying](ROADMAP.md#topic-persistence) | C | 0 |
| 37.3 | [Rollback DSU как откатываемая структура](ROADMAP.md#topic-rollback-dsu) | C | 0 |
| 37.4 | [Полная offline dynamic connectivity](ROADMAP.md#topic-dynamic-connectivity) | C | 0 |
| 38.1 | [Линейные переходы DP и monotone CHT](ROADMAP.md#topic-monotone-cht) | B | 0 |
| 38.2 | [Li Chao Tree](ROADMAP.md#topic-li-chao) | C | 0 |
| 38.3 | [Divide-and-conquer optimization DP](ROADMAP.md#topic-divide-conquer-dp) | C | 0 |
| 38.4 | [Оптимизация Кнута для interval DP](ROADMAP.md#topic-knuth) | C | 0 |
| 39.1 | [Матричное возведение и линейные переходы](ROADMAP.md#topic-matrix-exponentiation) | C | 0 |
| 39.2 | [Метод Гаусса над полями и GF(2)](ROADMAP.md#topic-gaussian-elimination) | C | 0 |
| 39.3 | [Линейный XOR-базис](ROADMAP.md#topic-xor-basis) | C | 0 |
| 39.4 | [Свертка полиномов, FFT и NTT](ROADMAP.md#topic-convolution) | C | 0 |
| 40.1 | [Дискретная вероятность, ожидание и probability DP](ROADMAP.md#topic-probability) | B | 0 |
| 40.2 | [Рандомизированные алгоритмы и вероятность ошибки](ROADMAP.md#topic-randomized) | C | 0 |
| 40.3 | [Интерактивные задачи и query complexity](ROADMAP.md#topic-interactive) | C | 0 |
| 40.4 | [Communication, double-run и two-step задачи](ROADMAP.md#topic-communication) | C | 0 |
| 40.5 | [Batch constructive со scoring/checker](ROADMAP.md#topic-scored-constructive) | C | 0 |
| 40.7 | [Open-test Batch](ROADMAP.md#topic-open-test-batch) | C | 0 |

Тема [40.6 OutputOnly](ROADMAP.md#topic-output-only) не включена в карту: в репозитории пока нет подтвержденного
официального набора открытых input-файлов и правил отправки output-файлов. Она станет отслеживаемой только вместе с
реальным checkpoint, а не по одной прочитанной теории.

## Целевые уровни

К началу отборов:

- темы `A0/A1` - преимущественно уровень `3`, ключевые темы постепенно закрепляются на `4`;
- темы `B` - уровень `1-2`;
- темы `C` допустимо оставить на `0`, если они не нужны для конкретной олимпиады.

После прохождения отборов:

- темы `A0/A1` закрепляются на уровне `4`;
- темы `B` поднимаются до `3`;
- выбранные под конкретные финалы темы `C` поднимаются до `2-3`.

## Диагностический baseline

Заполнить после двух смешанных контестов, не по памяти.

| Метрика                            | Контест 1 | Контест 2 |     Цель к октябрю |
| ---------------------------------- | --------: | --------: | -----------------: |
| Решено задач                       |         - |         - | зависит от формата |
| Время до первой AC                 |         - |         - |        <= 25-35 мин |
| Попыток до первой AC               |         - |         - |                <= 2 |
| Задач с найденной идеей, но без AC |         - |         - |              <= 1-2 |
| WA                                 |         - |         - |         тренд вниз |
| TLE/MLE/RE                         |         - |         - |                0-1 |
| Подсказок в upsolve                |         - |         - | фиксировать честно |
| Темы, не распознанные за 20 минут  |         - |         - |             список |

## Недельный журнал

Копировать блок на каждую неделю.

### Неделя YYYY-MM-DD - YYYY-MM-DD

- Плановые темы:
- Решено `Core/Extra`:
- Изменения уровней, например `6: 2 -> 3`:
- Контесты и результат:
- Upsolve завершён:
- Полезные выводы, если они были, добавлены в [`NOTES.md`](NOTES.md):
- Единственный главный приоритет следующей недели:

## Заметки

Признаки распознавания, нетривиальные идеи и собственные ошибки записываются свободными строками в [`NOTES.md`](NOTES.md). Дублировать их в карте тем не нужно.

## История контестов

| Дата | Контест/олимпиада | Длительность | Решено | Штраф/баллы | Первая AC | Upsolve |
| ---- | ----------------- | -----------: | -----: | ----------: | --------: | :-----: |
| -    | -                 |            - |      - |           - |         - |    -    |

## Метрики, которые действительно важны

1. Доля задач, решённых без подсказки.
2. Время от чтения до правильной модели, отдельно от времени кодирования.
3. Доля контестов с завершённым upsolve.
4. Число повторяющихся ошибок одного класса.
5. Успех повторного решения через 7-14 дней.
6. Стабильность Java-шаблонов под временем.

Общее число accepted полезно только вместе с этими метриками.
