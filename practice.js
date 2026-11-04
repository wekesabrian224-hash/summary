const first = "Lucky";
const course = "Software Engineering";

// Joining and inserting values (template literal: use backticks)
console.log(first + " studies " + course);
console.log(`${first} studies ${course}`);   // cleaner, preferred
console.log(`2 + 3 = ${2 + 3}`);             // any expression works inside ${}

// Common methods
const text = "  Hello, World  ";
console.log(text.trim());                    // "Hello, World"
console.log(text.toUpperCase());             // "  HELLO, WORLD  "
console.log(text.toLowerCase());             // "  hello, world  "
console.log(text.replace("World", "Nairobi"));
console.log("a,b,c".split(","));             // ['a', 'b', 'c']
console.log(["a", "b"].join("-"));           // "a-b"  (join belongs to arrays)
console.log(first.length);                   // 5

// Indexing and slicing
console.log(first[0]);                  // "L"
console.log(first[first.length - 1]);   // "y"
console.log(first.slice(1, 4));         // "uck"

// Strings are immutable here too
// first[0] = "l";   // silently does nothing (or errors in strict mode)
const lowered = "l" + first.slice(1);   // build a new string instead
console.log(lowered);                   // "lucky"



const score = 72;

if (score >= 80) {
  console.log("Distinction");
} else if (score >= 60) {
  console.log("Pass");
} else {
  console.log("Fail");
}

// Combining conditions
const age = 20;
const hasId = true;

if (age >= 18 && hasId) {
  console.log("Entry allowed");
}

// Checking membership
const role = "admin";
if (["admin", "editor"].includes(role)) {
  console.log("Can edit");
}

// One-line version (ternary)
const status = age >= 18 ? "adult" : "minor";
console.log(status);

// Truthy and falsy: these count as false
// 0, "", null, undefined, NaN (and false itself)
const name = "";
if (!name) {
  console.log("Name is empty");
}

// switch: useful when comparing one value to many options
const day = "Tue";
switch (day) {
  case "Sat":
  case "Sun":
    console.log("Weekend");
    break;
  default:
    console.log("Weekday");
}