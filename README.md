# The World in One Day — 26 November 2026

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/littleghoul/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard)
[![reward](https://make.fun/badge/news-image-20261126/littleghoul/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126)

One image that sums up the world's news of Thursday 26 November 2026:
32 verified stories from every region and every field, drawn as a newspaper
front page — "THE WORLD IN ONE DAY".

Bounty: [Sum up 26 November's world news in one image](https://make.fun/bounty/news-image-20261126)
($100, top 50 places; 1st $20, 2nd $12, 3rd $6, 4th–10th $2, 11th–50th $1.20)

## The 32 stories

1. Markets reel as US tariff plan sinks in — Nasdaq nears bear market after Trump's new duties on 14 partners
2. Kim orders wider spread of tactical nuclear arms — North Korea's leader says nuclear-material output is expanding
3. Ukraine hits Russian air base, damages five planes — Kyiv says the strike hit a major base deep inside Russia
4. Houthis hit Saudi Arabia's biggest oil refinery — Brent crude climbs to $94.81 as supply fears grow
5. North Korea expels Swiss diplomat in sanctions row — Pyongyang orders envoy out weeks after Bern reopened office
6. Dozens of nations urge Russia to stop riot-agent use — States demand halt to alleged chemical agent in Ukraine war
7. Murmansk governor held in corruption probe — Russian regional chief in pre-trial custody for two months
8. Second judge blocks Trump's birthright order — US court halts newest curbs on birthright citizenship
9. Israeli strike kills senior Hamas official in Gaza — Airstrike hits apartment; official's family also killed
10. Storm threatens 1.76m Palestinians in shelters — Gaza media office warns of flooding in makeshift camps
11. US and Russia return nine Ukrainian children — Children reunited with families at Melania Trump's urging
12. Sudan drone strikes kill 19 civilians — Attacks hit Blue Nile state, reports say
13. 31 killed in Cairo fuel-tanker fire — Tanker overturns on crowded highway and bursts into flames
14. Lebanon to open second international airport — New northern airport aims to lift the poorer north
15. China presses Dutch on fair business climate — Beijing raises Nexperia chip dispute with the Netherlands
16. UN warns of widening atrocity-crime risk in Gaza — Rights chief Türk says risk against Palestinians is growing
17. UN warns of more violence in western Nigeria — Rights chief raises alarm over attacks in the region
18. Bangladesh garment workers win 36% pay rise — Wage hike agreed for millions of factory workers
19. Bank of Korea raises rate to 3.25% — Seoul resumes tightening as AI export boom runs hot
20. Asia shares bounce; Nikkei up 1.6% — Kospi gains 1.9% as Wall Street fights back from deep lows
21. Nvidia down 3.9% to $149.30 — Chip giant now $2.3tn below its October peak
22. Anthropic shares fall below $83 IPO price — Record listing sours days after six-times oversubscription
23. Uber names Rakesh Ranjan India chief — Outsider takes over India and South Asia from January
24. US intel flags China watch on Alice Huang — Officials say Beijing may have tracked her in Jensen affair
25. 'BrainBot' nanorobot crosses blood-brain barrier — Gas-propelled bots deliver cancer drug in mice
26. Australian telescope begins galaxy census — 4MOST starts mapping millions of stars and galaxies
27. Kuala Lumpur sues Google for $146m — Malaysia claims bad content spread on its platforms
28. Puerto Rico's Barreto crowned Miss Universe — Jennifer Barreto is the first married winner of the title
29. Lille stun Bayern 2-1 in Champions League — Bayern's unbeaten run ends on an own goal in France
30. New York postpones Thanksgiving parade — Major storm forces Macy's parade to be delayed
31. Kenya discharges last Ebola patient — DRC death toll passes 5,300 in the outbreak
32. Norway court voids disputed oil licences — Supreme court rules climate-challenged permits invalid

Sources: Reuters, AFP, AP, CBS News, United Nations.

## Layout

The picture is a newspaper front page, 1024×1024, headed "THE WORLD IN
ONE DAY" with the date. Below the masthead the 32 stories sit in a grid of
4 columns × 8 rows of cards, in the same order as the list above: the top
row carries the day's biggest stories (markets, North Korea, Ukraine, the
Houthis), and the rows below cover the Middle East, Asia, markets, science
and sport. Each card has a coloured bar on its left edge that marks its
field — world politics, markets, science, culture and sport each have their
own colour — so the mix of the day is visible at a glance. Every headline
on the image matches one of the 32 stories listed above, word for word.

## How it runs

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` byte for byte to `/output/entry.png` (or
`$MAKEFUN_OUTPUT_DIR/entry.png` when set), then reads the written file back
and checks its byte count and SHA-256 digest against the original. Before
writing it also reads the PNG header and requires the picture to be
1024×1024. No network, no randomness — two runs write identical bytes.

To verify locally, run `python3 main.py` twice: both runs print
`wrote 143669 bytes to /output/entry.png (1024x1024, sha256
d11d5ea1e7ffac9cbb8d47a31677d6045a1fc70e26433ca28e7569fea62f306a)`,
and `sha256sum /output/entry.png` matches the hash of `entry.png` in this
repository.

## Files

- `entry.png` — the image, 1024×1024
- `main.py` — the program that places it at `/output/entry.png`
- `README.md` — this file
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.
