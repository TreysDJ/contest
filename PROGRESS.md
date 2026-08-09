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
| 1 | [Сложность и Java](ROADMAP.md#topic-complexity-java) | A0 | 0 |
| 2 | [Перебор и отсечения](ROADMAP.md#topic-bruteforce) | A0 | 0 |
| 3 | [Сортировка и сжатие координат](ROADMAP.md#topic-sorting-compression) | A0 | 0 |
| 4 | [Map, Set и частоты](ROADMAP.md#topic-maps-sets) | A0 | 0 |
| 5 | [Стек, очередь и дек](ROADMAP.md#topic-stack-queue-deque) | A0 | 0 |
| 6 | [Priority queue и heap](ROADMAP.md#topic-priority-queue) | A0 | 0 |
| 7.1 | [Префиксные суммы и 2D-префиксы](ROADMAP.md#topic-prefix-sums) | A1 | 0 |
| 7.2 | [Массив разностей](ROADMAP.md#topic-difference-array) | A1 | 0 |
| 8 | [Два указателя](ROADMAP.md#topic-two-pointers) | A1 | 0 |
| 9 | [Sliding window и монотонный дек](ROADMAP.md#topic-sliding-window) | A1 | 0 |
| 10 | [Монотонный стек](ROADMAP.md#topic-monotonic-stack) | A1 | 0 |
| 11 | [Sweep line](ROADMAP.md#topic-sweep-line) | A1 | 0 |
| 12 | [Binary search и поиск по ответу](ROADMAP.md#topic-binary-search) | A1 | 0 |
| 13 | [Жадные алгоритмы и доказательство](ROADMAP.md#topic-greedy) | A1 | 0 |
| 14 | [Биты и маски](ROADMAP.md#topic-bitmasks) | A1 | 0 |
| 15 | [Теория чисел](ROADMAP.md#topic-number-theory) | A1 | 0 |
| 16 | [Модульная арифметика и комбинаторика](ROADMAP.md#topic-modular-combinatorics) | A1 | 0 |
| 17.1 | [Префикс-функция, Z-функция и хеширование](ROADMAP.md#topic-prefix-z-hash) | A1 | 0 |
| 17.2 | [Trie](ROADMAP.md#topic-trie) | A1 | 0 |
| 18.1 | [Обходы графа](ROADMAP.md#topic-graph-traversals) | A1 | 0 |
| 18.2 | [DSU](ROADMAP.md#topic-dsu) | A1 | 0 |
| 19 | [Кратчайшие пути](ROADMAP.md#topic-shortest-paths) | A1 | 0 |
| 20 | [Деревья и LCA](ROADMAP.md#topic-trees-lca) | A1 | 0 |
| 21.1 | [Базовое DP](ROADMAP.md#topic-basic-dp-core) | A1 | 0 |
| 21.2 | [DAG и топологический порядок](ROADMAP.md#topic-dag) | A1 | 0 |
| 22 | [Fenwick tree](ROADMAP.md#topic-fenwick) | A1 | 0 |
| 23 | [Static RMQ и sparse table](ROADMAP.md#topic-static-rmq) | A1 | 0 |
| 24 | [Segment tree и lazy propagation](ROADMAP.md#topic-segment-tree) | A1 | 0 |
| 25.1 | [Геометрические предикаты и пересечения](ROADMAP.md#topic-geometry-predicates) | B | 0 |
| 25.2 | [Многоугольники и point-in-polygon](ROADMAP.md#topic-polygons) | B | 0 |
| 25.3 | [Выпуклая оболочка](ROADMAP.md#topic-convex-hull) | B | 0 |
| 25.4 | [Вращающиеся калиперы](ROADMAP.md#topic-rotating-calipers) | C | 0 |
| 25.5 | [Геометрический sweep](ROADMAP.md#topic-geometry-sweep) | C | 0 |
| 25.6 | [Пара ближайших точек](ROADMAP.md#topic-closest-pair) | C | 0 |
| 26.1 | [SCC и граф конденсации](ROADMAP.md#topic-scc) | B | 0 |
| 26.2 | [2-SAT](ROADMAP.md#topic-two-sat) | B | 0 |
| 26.3 | [Мосты и двусвязность](ROADMAP.md#topic-bridges-biconnected) | B | 0 |
| 27.1 | [Минимальные остовы](ROADMAP.md#topic-mst) | B | 0 |
| 27.2 | [Офлайн-активация через DSU](ROADMAP.md#topic-dsu-offline-activation) | B | 0 |
| 28.1 | [DP по отрезкам](ROADMAP.md#topic-interval-dp) | B | 0 |
| 28.2 | [Слоистое DP](ROADMAP.md#topic-layered-grid-dp) | B | 0 |
| 28.3 | [DP по поддеревьям](ROADMAP.md#topic-subtree-dp) | B | 0 |
| 28.4 | [Rerooting DP](ROADMAP.md#topic-rerooting) | B | 0 |
| 29.1 | [DP по подмножествам](ROADMAP.md#topic-subset-dp-core) | B | 0 |
| 29.2 | [Digit DP](ROADMAP.md#topic-digit-dp) | B | 0 |
| 29.3 | [Profile DP](ROADMAP.md#topic-profile-dp) | B | 0 |
| 29.4 | [SOS DP](ROADMAP.md#topic-sos-dp) | C | 0 |
| 30.1 | [Статическое декартово дерево](ROADMAP.md#topic-cartesian-tree) | B | 0 |
| 30.2 | [Explicit-key treap](ROADMAP.md#topic-explicit-treap) | B | 0 |
| 30.3 | [Implicit treap](ROADMAP.md#topic-implicit-treap) | B | 0 |
| 30.4 | [Bitwise trie](ROADMAP.md#topic-bitwise-trie) | B | 0 |
| 31.1 | [Двудольное паросочетание](ROADMAP.md#topic-bipartite-matching) | B | 0 |
| 31.2 | [Максимальный поток и минимальный разрез](ROADMAP.md#topic-max-flow) | B | 0 |
| 31.3 | [Поток минимальной стоимости](ROADMAP.md#topic-min-cost-flow) | C | 0 |
| 32.1 | [Ахо-Корасик](ROADMAP.md#topic-aho-corasick) | B | 0 |
| 32.2 | [Алгоритм Манакера](ROADMAP.md#topic-manacher) | B | 0 |
| 32.3 | [Suffix array и LCP](ROADMAP.md#topic-suffix-array) | B | 0 |
| 32.4 | [Суффиксный автомат](ROADMAP.md#topic-suffix-automaton) | C | 0 |
| 33.1 | [Heavy-light decomposition](ROADMAP.md#topic-hld) | B | 0 |
| 33.2 | [Центроидная декомпозиция](ROADMAP.md#topic-centroid-decomposition) | B | 0 |
| 33.3 | [Small-to-large и DSU on tree](ROADMAP.md#topic-small-to-large) | B | 0 |
| 34.1 | [P/N-позиции](ROADMAP.md#topic-pn-games) | B | 0 |
| 34.2 | [Minimax](ROADMAP.md#topic-minimax) | B | 0 |
| 34.3 | [Nim и Sprague-Grundy](ROADMAP.md#topic-nim-sg) | B | 0 |
| 34.4 | [Игры с циклами](ROADMAP.md#topic-cyclic-games) | C | 0 |
| 35 | [Meet-in-the-middle](ROADMAP.md#topic-meet-in-the-middle) | B | 0 |
| 36.1 | [Sqrt decomposition по блокам](ROADMAP.md#topic-sqrt-blocks) | C | 0 |
| 36.2 | [Алгоритм Мо](ROADMAP.md#topic-mo) | C | 0 |
| 37.1 | [Rollback по дереву версий](ROADMAP.md#topic-version-rollback) | C | 0 |
| 37.2 | [Персистентные структуры](ROADMAP.md#topic-persistence) | C | 0 |
| 37.3 | [Rollback DSU и dynamic connectivity](ROADMAP.md#topic-dynamic-connectivity) | C | 0 |
| 38.1 | [Monotone CHT](ROADMAP.md#topic-monotone-cht) | B | 0 |
| 38.2 | [Li Chao Tree](ROADMAP.md#topic-li-chao) | C | 0 |
| 38.3 | [Divide-and-conquer optimization DP](ROADMAP.md#topic-divide-conquer-dp) | C | 0 |
| 38.4 | [Оптимизация Кнута](ROADMAP.md#topic-knuth) | C | 0 |
| 39.1 | [Матричное возведение](ROADMAP.md#topic-matrix-exponentiation) | C | 0 |
| 39.2 | [Метод Гаусса и GF(2)](ROADMAP.md#topic-gaussian-elimination) | C | 0 |
| 39.3 | [Линейный XOR-базис](ROADMAP.md#topic-xor-basis) | C | 0 |
| 39.4 | [Свертка, FFT и NTT](ROADMAP.md#topic-convolution) | C | 0 |
| 40.1 | [Вероятность и математическое ожидание](ROADMAP.md#topic-probability) | B | 0 |
| 40.2 | [Рандомизированные алгоритмы](ROADMAP.md#topic-randomized) | C | 0 |
| 40.3 | [Интерактивные задачи](ROADMAP.md#topic-interactive) | C | 0 |
| 40.4 | [Communication и double-run](ROADMAP.md#topic-communication) | C | 0 |
| 40.5 | [Batch constructive со scoring](ROADMAP.md#topic-scored-constructive) | C | 0 |
| 40.7 | [Open-test Batch](ROADMAP.md#topic-open-test-batch) | C | 0 |

Тема [40.6 OutputOnly](ROADMAP.md#topic-output-only) не включена в карту: в репозитории пока нет подтвержденного
официального набора открытых input-файлов и правил отправки output-файлов. Она станет отслеживаемой только вместе с
реальным checkpoint, а не по одной прочитанной теории.

## Целевые уровни

К началу отборов:

- темы `A0/A1` — преимущественно уровень `3`, ключевые темы постепенно закрепляются на `4`;
- темы `B` — уровень `1–2`;
- темы `C` допустимо оставить на `0`, если они не нужны для конкретной олимпиады.

После прохождения отборов:

- темы `A0/A1` закрепляются на уровне `4`;
- темы `B` поднимаются до `3`;
- выбранные под конкретные финалы темы `C` поднимаются до `2–3`.

## Диагностический baseline

Заполнить после двух смешанных контестов, не по памяти.

| Метрика                            | Контест 1 | Контест 2 |     Цель к октябрю |
| ---------------------------------- | --------: | --------: | -----------------: |
| Решено задач                       |         — |         — | зависит от формата |
| Время до первой AC                 |         — |         — |        ≤ 25–35 мин |
| Попыток до первой AC               |         — |         — |                ≤ 2 |
| Задач с найденной идеей, но без AC |         — |         — |              ≤ 1–2 |
| WA                                 |         — |         — |         тренд вниз |
| TLE/MLE/RE                         |         — |         — |                0–1 |
| Подсказок в upsolve                |         — |         — | фиксировать честно |
| Темы, не распознанные за 20 минут  |         — |         — |             список |

## Недельный журнал

Копировать блок на каждую неделю.

### Неделя YYYY-MM-DD — YYYY-MM-DD

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
| —    | —                 |            — |      — |           — |         — |    —    |

## Метрики, которые действительно важны

1. Доля задач, решённых без подсказки.
2. Время от чтения до правильной модели, отдельно от времени кодирования.
3. Доля контестов с завершённым upsolve.
4. Число повторяющихся ошибок одного класса.
5. Успех повторного решения через 7–14 дней.
6. Стабильность Java-шаблонов под временем.

Общее число accepted полезно только вместе с этими метриками.
