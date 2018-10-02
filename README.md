# sts_renamer

---

## About 

This script is designed to properly encode / decode folder names based on the color and number structured used by the 4MS Stereo Trigger Sampler module.

The decode option will rename prefixes to a number index (White to 00, Red-1 to 11, etc) and the encode option will rename number indexes to the proper color and number (2 to Orange, 15 to Cyan-1, etc).

---

## How to Use


**IMPORTANT: BACK UP YOU SD CARD BEFORE DOING ANYTHING!**  
I wrote this script based on my own setup / needs therefore I haven't tested it in every possible way (altough the worst it can happen is that you folder names will end up getting messed up).


**Basic Method:**  
```python3 path/to/sts_renamer.py```

**Selecting the operation via arguments:**  
```python3 path/to/sts_renamer.py -op encode``` or ```python3 path/to/sts_renamer.py -op decode``` 

---

## Limitations

- Developed and tested only on macOS
- SD card must be named "STS"

---


**Ícaro Ferre**  
@icaroferre  
[spektroaudio.com](http://spektroaudio.com/)