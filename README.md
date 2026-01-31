[README.md](https://github.com/user-attachments/files/24983878/README.md)
# Adult Age Calculator

A simple Python program that calculates adult status based on age input.

## Features

· Calculates years remaining until adulthood (if under 18)
· Shows years passed since adulthood (if over 18)
· Simple command-line interface
· No external libraries required

## How to Run

### Method 1
  ```bash
jupyter notebook adult-age-calculator.ipynb
```
### Method 2
```jupyter nbconvert --to python adult-age-calculator.ipynb
python adult-age-calculator.py
```

## Example Output
```

Adult Age Calculator
========================================
Enter your age: 16

========================================
You have 2 years left,
You will be adult in year 2028
======================================== 
 ```

## Another Example
```

Adult Age Calculator
========================================
Enter your age: 25

========================================
You became adult in year 2019,
7 years passed since adulthood
========================================
```

## Project Structure

adult-age-calculator/
├── age_calculator.ipynb    # Main program file
└── README.md           # This documentation file


## Requirements

· Python 3.x

## How It Works

1. Program asks user to enter their age
2. Compares the age with 18 (adulthood age)
3. Shows appropriate message based on the comparison
4. For ages under 18: shows years left and target year
5. For age 18: shows congratulatory message
6. For ages over 18: shows years passed since adulthood

## Author

Kamran Azarmehr - NeuralWhite

## License

MIT License - Feel free to use, modify, and distribute

## Notes

· This is a beginner-friendly Python project
· Great for learning basic Python syntax and logic
· Easy to extend with more features
· Perfect for GitHub portfolio

