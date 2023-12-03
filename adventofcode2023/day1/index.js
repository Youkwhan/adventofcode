const fs = require("node:fs")

function main(fileName) {
	fs.readFile(fileName, "utf8", function (err, data) {
		if (err) console.log(err.message)
		else {
			const parsedData = data.split("\n").map((line) => line.trim())

			const processedData = partOne(parsedData)
			const sum = processedData.reduce((acc, cur) => acc + cur, 0)
			console.log("PartOne Sum:", sum)

			const partTwoData = partTwo(parsedData)
			const sumPartTwo = partOne(partTwoData)
			const sum2 = sumPartTwo.reduce((acc, cur) => acc + cur, 0)
			console.log("Part Two Sum:", sum2)
		}
	})
	// function: grab the numbers
	function partOne(data) {
		return data.map((line) => {
			// for each line, filter out the numbers only
			const numbers = line.split("").filter((chr) => !isNaN(chr))
			const first = numbers[0]
			const second = numbers[numbers.length - 1]
			return Number(first + second)
		})
	}

	function partTwo(data) {
		const wordMatch = {
			zero: "z0ro",
			one: "o1e",
			two: "t2o",
			three: "th3ee",
			four: "fo4r",
			five: "f5ve",
			six: "s6x",
			seven: "s7ven",
			eight: "e8ght",
			nine: "n9ne",
		}
		return data.map((line) => {
			for (word in wordMatch) {
				const pattern = new RegExp(word, "g")
				line = line.replace(pattern, wordMatch[word])
			}
			return line
		})
	}
}

// main("./example.txt")
main("./example2.txt")
main("./input.txt")
