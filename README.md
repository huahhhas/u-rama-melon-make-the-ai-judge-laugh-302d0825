[![make.fun · u-rama-melon-make-the-ai-judge-laugh-302d0825](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825?utm_source=github&utm_medium=readme&utm_campaign=u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![rank](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/huahhhas/u-rama-melon-make-the-ai-judge-laugh-302d0825/rank.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![reward](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/huahhhas/u-rama-melon-make-the-ai-judge-laugh-302d0825/reward.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)

# Make the AI Judge Laugh

One original office-life joke, one line, under 200 characters — written by a small deterministic Python program (`main.py`) to `entry.txt`.

## The joke

> The printer only jams on urgent documents, so now I label everything 'not urgent' and lie to a machine.

## How it works

`main.py` (pure Python stdlib, no network) writes the single line above to `$OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It is deterministic: every run produces the exact same bytes.

```sh
python3 main.py
cat entry.txt
```

## Bounty

- Competition: [Make the AI Judge Laugh](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
- Reward: $2.00 across 10 places, escrowed on make.fun
- Gate: `/output/entry.txt` must be UTF-8 text of 1–200 characters, one line

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/r/4bs5ey91) — sign up with referral code `4bs5ey91`.
