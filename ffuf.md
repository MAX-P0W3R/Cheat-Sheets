![image](https://user-images.githubusercontent.com/30239728/165584996-35ef5e47-1e09-4cf0-964a-1b9cb2f2307a.png)
# Install
- git clone https://github.com/ffuf/ffuf.git
- cd ffuf
- go get
- go build

# Example Usage
```go
ffuf -w /path/to/wordlist -u https://target/FUZZ
```

# GET parameter fuzzing
```go
ffuf -w /path/to/paramnames.txt -u https://target/script.php?FUZZ=test_value -fs 4242
```
```go
fuff -w /path/to/values.txt -u https://target/script.php?valid_name=FUZZ -fc 401
```
