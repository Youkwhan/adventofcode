const fs = require("fs").promises

async function main(fileName) {
	try {
		const data = await fs.readFile(fileName, "utf8")
		const parsedData = data.split("\n").map((line) => {
			return line.split(":")[1].trim()
		})
		const validGameIDs = getValidGameIDs(parsedData)
		// console.log(validGameIDs)
		const sumOfIDs = validGameIDs.reduce((acc, cur) => acc + cur, 0)
		console.log(sumOfIDs)

		const powerSet = calculateMinimumPower(parsedData)
		console.log(powerSet)
	} catch (err) {
		console.log(err.message)
	}
}

// Part one, rtype: number[]
function getValidGameIDs(parsedData) {
	const bagLimits = {
		red: 12,
		green: 13,
		blue: 14,
	}

	const validGameIndices = []

	for (let gameIndex = 0; gameIndex < parsedData.length; gameIndex++) {
		const rounds = parsedData[gameIndex].split(";")
		let isValidGame = true

		for (const round of rounds) {
			const pairs = round.trim().split(",")

			const isValidRound = pairs.every((pair) => {
				const [count, color] = pair.trim().split(" ")
				return parseInt(count) <= bagLimits[color]
			})

			if (!isValidRound) {
				isValidGame = false
				break
			}
		}

		if (isValidGame) {
			validGameIndices.push(gameIndex + 1) // Game index starts at 1
		}
	}

	return validGameIndices
}

// Part Two
function calculateMinimumPower(parsedData) {
	let totalPower = 0

	for (const game of parsedData) {
		const rounds = game.split(";")

		let counts = { red: 0, green: 0, blue: 0 }

		for (const round of rounds) {
			const pairs = round.trim().split(",")
			for (const pair of pairs) {
				const [count, color] = pair.trim().split(" ")
				counts[color] = Math.max(counts[color], parseInt(count))
			}
		}

		const power = counts.red * counts.green * counts.blue
		totalPower += power
	}

	return totalPower
}

main("./example.txt")
main("./input.txt")
