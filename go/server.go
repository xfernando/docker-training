package main

import (
	"fmt"
	"html/template"
	"net/http"
	"os"
)

func main() {
	http.HandleFunc("/", homeHandler)
	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Println("Could not bind server to port 8080, exiting.")
	}
	fmt.Println("Server listening on port 8080.")
}

func homeHandler(w http.ResponseWriter, r *http.Request) {
	hostname, _ := os.Hostname()

	d := struct{ Host string }{hostname}
	t, err := template.ParseFiles("home.html")
	if err != nil {
		fmt.Fprintf(w, "Could not parse template: %v", err)
		return
	}
	t.Execute(w, d)
}
