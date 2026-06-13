// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    // 1. Integer variable declare kiya value store karne ke liye (public rakhne se yeh baher se read ho sakta hai)
    int256 public storedValue;

    // Contract start hote hi value ko 0 set karne ke liye
    constructor() {
        storedValue = 0;
    }

    // 2. Increment function jo value ko 1 barha deta hai
    function increment() public {
        storedValue += 1;
    }

    // 3. Decrement function jo value ko 1 kam kar deta hai
    function decrement() public {
        storedValue -= 1;
    }

    // 4. Read karne ke liye extra function (agar public variable ke ilawa alag se chahiye ho)
    function getValue() public view returns (int256) {
        return storedValue;
    }
}

