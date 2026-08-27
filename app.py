<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scientific Calculator</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: #1b1b1b;
            font-family: Arial, sans-serif;
        }

        .calculator {
            width: 360px;
            padding: 20px;
            background: #292929;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }

        #display {
            width: 100%;
            height: 75px;
            margin-bottom: 15px;
            padding: 10px;
            border: none;
            border-radius: 10px;
            background: #111;
            color: white;
            font-size: 28px;
            text-align: right;
        }

        .buttons {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
        }

        button {
            height: 55px;
            border: none;
            border-radius: 10px;
            font-size: 18px;
            cursor: pointer;
            background: #444;
            color: white;
        }

        button:active {
            transform: scale(0.95);
        }

        .scientific {
            background: #555;
        }

        .operator {
            background: #ff9500;
        }

        .equal {
            background: #2196f3;
        }

        .clear {
            background: #e53935;
        }
    </style>
</head>

<body>

<div class="calculator">

    <input type="text" id="display" readonly>

    <div class="buttons">

        <button class="clear" onclick="clearDisplay()">AC</button>
        <button onclick="deleteLast()">DEL</button>
        <button class="scientific" onclick="add('(')">(</button>
        <button class="scientific" onclick="add(')')">)</button>

        <button class="scientific" onclick="calculateFunction('sin')">sin</button>
        <button class="scientific" onclick="calculateFunction('cos')">cos</button>
        <button class="scientific" onclick="calculateFunction('tan')">tan</button>
        <button class="operator" onclick="add('/')">÷</button>

        <button class="scientific" onclick="calculateFunction('log')">log</button>
        <button class="scientific" onclick="calculateFunction('ln')">ln</button>
        <button class="scientific" onclick="squareRoot()">√</button>
        <button class="operator" onclick="add('*')">×</button>

        <button onclick="add('7')">7</button>
        <button onclick="add('8')">8</button>
        <button onclick="add('9')">9</button>
        <button class="operator
