const fs = require("node:fs")

function main(fileName) {
	fs.readFile(fileName, "utf8", function (err, data) {
		if (err) console.log(err.message)
		else {
			const parsedData = data.split("\n").map((line) => line.trim())

			const processedData = partOne(parsedData)
			const sum = processedData.reduce((acc, cur) => acc + cur, 0)
			console.log("PartOne Sum:", sum)

			const sumPartTwo = partTwo(parsedData)
			console.log("Part Two Sum:", sumPartTwo)
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

	function partTwo(data) {}
}

// main("./example.txt")
main("./example2.txt")
// main("./input.txt")
