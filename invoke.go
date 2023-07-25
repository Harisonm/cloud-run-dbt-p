package main
import (
        "fmt"
        "log"
        "net/http"
        "os"
        "os/exec"
)

type HandlerData struct {
        data string
        //whatever
    }

    
func (h *HandlerData) handler(w http.ResponseWriter, r *http.Request) {
        log.Print("helloworld: received a request")
cmd := exec.Command("dbt",h.data)
        log.Print(h.data)
        cmd.Stdout = os.Stdout
 cmd.Stderr = os.Stderr
 err := cmd.Run()
 if err != nil {
  log.Fatalf("cmd.Run() failed with %s\n", err)
 }
}

func main() {
        log.Print("helloworld: starting server...")
        //Create a data struct
        // add data to struct
        h := &HandlerData{...}

http.HandleFunc("/", handler())


port := os.Getenv("PORT")
        if port == "" {
                port = "8080"
        }
log.Printf("helloworld: listening on %s", port)
        log.Fatal(http.ListenAndServe(fmt.Sprintf(":%s", port), nil))
}