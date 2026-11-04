// classic for loop: start; condition; step
for (let i = 0; i < 5; i++) {      // 0, 1, 2, 3, 4
  console.log(i);
}

for (let i = 1; i <= 5; i++) {     // 1 to 5
  console.log(i);
}

for (let i = 0; i < 10; i += 2) {  // 0, 2, 4, 6, 8
  console.log(i);
}

// for...of loop over a string (or an array)
for (const letter of "Lucky") {
  console.log(letter);
}

// while loop: runs as long as the condition is true
let count = 3;
while (count > 0) {
  console.log("Countdown:", count);
  count--;                          // without this line, the loop never ends
}

// do...while: always runs at least once, then checks the condition
let tries = 0;
do {
  console.log("Attempt", tries + 1);
  tries++;
} while (tries < 2);

// break and continue
for (let n = 1; n < 10; n++) {
  if (n === 3) continue;            // skip 3
  if (n === 6) break;               // stop completely at 6
  console.log(n);                   // prints 1, 2, 4, 5
}

// Accumulator pattern
let total = 0;
for (let n = 1; n <= 5; n++) {
  total += n;
}
console.log("Sum:", total);         // 15

// Nested loop: multiplication table
for (let row = 1; row <= 3; row++) {
  let line = "";
  for (let col = 1; col <= 3; col++) {
    line += row * col + " ";
  }
  console.log(line);
}