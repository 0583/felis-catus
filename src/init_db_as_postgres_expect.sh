#! /usr/bin/expect

spawn sudo -u postgres createuser -h localhost -p 5432 -s felis -P
expect "Enter password for new role: "
send "123456\r"

expect "Enter it again: "
send "123456\r"

expect "Password: "
send "postgres\r"
