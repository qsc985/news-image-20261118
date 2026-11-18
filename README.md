[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/qsc985/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/qsc985/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

# World News — Wednesday 18 November 2026

A one-image summary of the world's news of Wednesday 18 November 2026,
built for the [make.fun](https://make.fun/bounty/news-image-20261118)
news-image-20261118 bounty.

## The image

A newspaper front page (1024×1024 PNG) with six stories from 18 November 2026,
each verified against that day's reporting:

- **Lead — Trump lands in Manila for Quad talks.** The US president arrived
  in the Philippines for talks with Quad allies, ahead of a visit to China
  to meet Xi Jinping.
- **Ukraine hits the Crimean bridge.** Kyiv said it damaged the bridge
  linking Russia to Crimea for a second day, as Russian strikes pounded
  bridges in Kyiv.
- **Israel taps Eisenkot to form government.** President Herzog asked
  ex-army chief Gadi Eisenkot to try to form a government, bypassing
  Benjamin Netanyahu.
- **Nvidia posts bumper results.** Strong quarterly earnings; the firm said
  former chief Jensen Huang will not return.
- **Dhoni retires from the IPL.** MS Dhoni ended his playing career and
  will become a mentor at Chennai Super Kings.
- **Briefs.** UK and Australia sanction firms over West Bank settlements;
  Cyclone Akvan set to turn severe over the Bay of Bengal.

## How it is built

`draw_news.py` draws `entry.png` with Pillow (run once, in the build
session). The entry program `main.py` is standard library only: it copies
`entry.png` to `/output/entry.png`, so both graded runs write identical
bytes with no network.

```sh
python3 draw_news.py        # regenerate entry.png (build time only)
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

## License

MIT — see `LICENSE`.
