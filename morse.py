from typing import Callable
import numpy as np

JITTER_LEVEL: float = 0.03 # 98% of human reaction is within 30ms (assumption)
JITTER_MODEL: Callable[[bool],float] = lambda jitter: np.random.default_rng().normal(0, JITTER_LEVEL) if jitter else 0

def calculate_wpm(dit_time: float) -> int:
    """
    Calculates the words per minute (wpm) based on the given dit time in seconds.

    Parameters:
    - dit_time (float): The duration of a dit in seconds.

    Returns:
    - int: The words per minute value.

    Example:
    >>> calculate_wpm(0.12)
    20
    """
    wpm = int(1.2 / dit_time)
    return wpm

def calculate_dit_time(wpm: int) -> float:
    """
    Calculates the duration of a dit (short signal) in Morse code based on the given words per minute (wpm).

    Parameters:
    - wpm (int): The words per minute value to calculate the dit time for.

    Returns:
    - float: The duration of a dit in seconds.

    Example:
    >>> calculate_dit_time(20)
    0.12
    """
    dit_duration = 1.2 / wpm
    return dit_duration

def dit_tone(f: float, Fs: float, wpm: int, jitter: bool = False) -> np.array:
    """
    Generates a sine wave for a dit (short signal) in Morse code.

    Parameters:
    - f (float): The frequency of the sine wave.
    - Fs (float): The sampling rate of the sine wave.
    - wpm (int): The words per minute value to calculate the dit time for.
    - jitter (bool): Whether to add jitter to the signal.

    Returns:
    - np.array: The sine wave for a dit.

    Example:
    >>> dit_tone(1000.0, 8000.0, 20)
    array([ 0.        ,  0.58778525,  0.95105652,  0.95105652,  0.58778525,
            0.        , -0.58778525, -0.95105652, -0.95105652, -0.58778525])
    """
    dit_duration = calculate_dit_time(wpm) + JITTER_MODEL(jitter)
    t = np.linspace(0, dit_duration, int(dit_duration * Fs), endpoint=False)
    dit = np.sin(2 * np.pi * f * t)
    return dit

def dah_tone(f: float, Fs: float, wpm: int, jitter: bool = False) -> np.array:
    """
    Generates a sine wave for a dah (long signal) in Morse code.

    Parameters:
    - f (float): The frequency of the sine wave.
    - Fs (float): The sampling rate of the sine wave.
    - wpm (int): The words per minute value to calculate the dit time for.
    - jitter (bool): Whether to add jitter to the signal.

    Returns:
    - np.array: The sine wave for a dah.

    Example:
    >>> dah_tone(1000, 8000, 20)
    array([ 0.        ,  0.95105652,  0.58778525,  0.        , -0.58778525,
           -0.95105652, -0.95105652, -0.58778525,  0.        ,  0.58778525])
    """
    dit_duration = calculate_dit_time(wpm)
    dah_duration = 3 * dit_duration + JITTER_MODEL(jitter)
    t = np.linspace(0, dah_duration, int(dah_duration * Fs), endpoint=False)
    dah = np.sin(2 * np.pi * f * t)
    return dah

def space(Fs: float, wpm: int, jitter: bool = False) -> np.array:
    """
    Generates a space between two Morse code signals.

    Parameters:
    - Fs (float): The sampling rate of the sine wave.
    - wpm (int): The words per minute value to calculate the dit time for.
    - jitter (bool): Whether to add jitter to the signal.

    Returns:
    - np.array: The sine wave for a space.

    Example:
    >>> space(8000, 20)
    array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
    """
    dit_duration = calculate_dit_time(wpm) 
    space_duration = dit_duration + JITTER_MODEL(jitter)
    t = np.linspace(0, space_duration, int(space_duration * Fs), endpoint=False)
    space = np.zeros_like(t)
    return space

def letter_space(Fs: float, wpm: int, jitter: bool = False) -> np.array:
    """
    Generates a space between two letters in Morse code.

    Parameters:
    - Fs (float): The sampling rate of the sine wave.
    - wpm (int): The words per minute value to calculate the dit time for.
    - jitter (bool): Whether to add jitter to the signal.

    Returns:
    - np.array: The sine wave for a letter space.

    Example:
    >>> letter_space(8000, 20)
    array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
    """
    dit_duration = calculate_dit_time(wpm)
    letter_space_duration = 3 * dit_duration + JITTER_MODEL(jitter)
    t = np.linspace(0, letter_space_duration, int(letter_space_duration * Fs), endpoint=False)
    letter_space = np.zeros_like(t)
    return letter_space

def word_space(Fs: float, wpm: int, jitter: bool = False) -> np.array:
    """
    Generates a space between two words in Morse code.

    Parameters:
    - Fs (float): The sampling rate of the sine wave.
    - wpm (int): The words per minute value to calculate the dit time for.
    - jitter (bool): Whether to add jitter to the signal.

    Returns:
    - np.array: The sine wave for a word space.

    Example:
    >>> word_space(8000, 20)
    array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
    """
    dit_duration = calculate_dit_time(wpm)
    word_space_duration = 6 * dit_duration + JITTER_MODEL(jitter)
    t = np.linspace(0, word_space_duration, int(word_space_duration * Fs), endpoint=False)
    word_space = np.zeros_like(t)
    return word_space

def encode_letter(letter: str, f: float, Fs: float, wpm: int, jitter: bool = False) -> np.array:
    """
    Encodes a letter in Morse code.

    Parameters:
    - letter (str): The letter to encode.
    - f (float): The frequency of the sine wave.
    - Fs (float): The sampling rate of the sine wave.
    - wpm (int): The words per minute value to calculate the dit time for.
    - jitter (bool): Whether to add jitter to the signal.

    Returns:
    - np.array: The sine wave representing the encoded letter.

    """
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
        ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
        ' ': '/'
    }

    letter = letter.upper()
    if letter in morse_code:
        morse = morse_code[letter]
        encoded_letter = np.array([])
        for symbol in morse:
            if symbol == '.':
                dit = dit_tone(f, Fs, wpm)
                encoded_letter = np.concatenate((encoded_letter, dit, space(Fs, wpm)))
            elif symbol == '-':
                dah = dah_tone(f, Fs, wpm)
                encoded_letter = np.concatenate((encoded_letter, dah, space(Fs, wpm)))
            elif symbol == '/':
                encode_letter= np.concatenate((encoded_letter, word_space(Fs, wpm)))
        encoded_letter = np.concatenate((encoded_letter, letter_space(Fs, wpm)))
        return encoded_letter
    else:
        return np.array([])
    
def encode_message(message: str, f: float, Fs: float, wpm: int, jitter: bool = False) -> np.array:
    """
    Encodes a message in Morse code.

    Parameters:
    - message (str): The message to encode.
    - f (float): The frequency of the sine wave.
    - Fs (float): The sampling rate of the sine wave.
    - wpm (int): The words per minute value to calculate the dit time for.
    - jitter (bool): Whether to add jitter to the signal.

    Returns:
    - np.array: The sine wave representing the encoded message.

    """
    encoded_message = np.array([])

    for letter in message:
        if letter == ' ':
            encoded_message = np.concatenate((encoded_message, word_space(Fs, wpm, jitter)))
        else:
            encoded_letter = encode_letter(letter, f, Fs, wpm, jitter)
            encoded_message = np.concatenate((encoded_message, encoded_letter))
    return encoded_message

