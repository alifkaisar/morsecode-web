# MorseCode-encode
_I am a junior Python developer. I will upload my portfolio on this GitHub account. Feel free to give suggestions on my portfolio, such as improving the code or providing additional features. It will make me very happy and will improve my programming skills._

## Introduction
Morse code is a method used in telecommunication to encode text characters as standardized sequences of two different signal durations, called dots and dashes, or dits and dahs [(Wikipedia)](https://en.wikipedia.org/wiki/Morse_code#). The Morse code is named after Samuel F.B. Morse who was the inventor and early developer of the system adopted for electrical telegraphy.

Each Morse code symbol is formed by a sequence of dits (.) and dahs (-). The dit duration can vary for signal clarity and operator skill, but for any one message, once established it is the basic unit of time measurement in Morse code. The duration of a dah is three times the duration of a dit. Each dit or dah within an encoded character is followed by a period of signal absence, called a space, equal to the dit duration [(Wikipedia)](https://en.wikipedia.org/wiki/Morse_code#).

## International Morse Code
This program uses the International Telecommunication Union (ITU) standard Morse code. Morse code was standardized by the International Telegraphy Congress and became the standard used by the ITU. More information on [Wikipedia](https://en.wikipedia.org/wiki/Morse_code#International_Morse_code) and [ITU](https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1677-1-200910-I!!PDF-E.pdf).

## Morse Code Alphabet
Here is the Morse code in letters, numbers, and punctuation. For more, see [Wikipedia](https://en.wikipedia.org/wiki/Morse_code#Letters,_numbers,_punctuation,_prosigns_for_Morse_code_and_non-Latin_variants). If there is a character that does not have a code, it will be replaced by a '#' sign.

**1. Letters**
| Letter | Code      | Letter | Code      | Letter | Code      |
| :---:  | :---:     | :---:  | :---:     | :---:  | :---:     |
| A      | .-        | J      | .---      | S      | ...       |
| B      | -...      | K      | -.-       | T      | -         |
| C      | -.-.      | L      | .-..      | U      | ..-       |
| D      | -..       | M      | --        | V      | ...-      |
| E      | .         | N      | -.        | W      | .--       |
| F      | ..-.      | O      | ---       | X      | -..-      |
| G      | --.       | P      | .--.      | Y      | -.--      |
| H      | ....      | Q      | --.-      | Z      | --..      |
| I      | ..        | R      | .-.       |        |           |

**2. Number**
| Number | Code      | Number | Code      | Number | Code      |
| :---:  | :---:     | :---:  | :---:     | :---:  | :---:     |
| 0      | -----     | 4      | ....-     | 8      | ---..     |
| 1      | .----     | 5      | .....     | 9      | ----.     |
| 2      | ..---     | 6      | -....     |        |           |
| 3      | ...--     | 7      | --...     |        | -         |

**3. Punctuation**
| Punctuation | Code      | Punctuation | Code      | Punctuation | Code      |
|    :---:    | :---:     |    :---:    | :---:     |    :---:    | :---:     |
| ;           | -.-.-.    | ,           | --..--    | :           | ---...    |
| -           | -....-    | !           | -.-.--    | +           | .-.-.     |
| $           | ...-..-   | )           | -.--.-    | "           | .-..-.    |
| ?           | ..--..    | .           | .-.-.-    | =           | -...-     |
| /           | -..-.     | '           | .----.    | _           | ..--.-    |
| &           | .-...     | (           | -.--.     | @           | .--.-.    |

## Website
- The website is built using Flask in Python. 
- Only uses one route.
- The use of forms on this website uses WTForm and Flask-WTF. 
- The website display uses Bootstrap CSS framework.
- HTML files are contained in the templates folder.

## How to Use:
Input text and press the Encode button, The morse code will display under input text.
