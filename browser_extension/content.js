console.log("De Best Password Manager extension is running");
const passwordFields = document.querySelectorAll('input[type="password"]');
console.log("Password fields found:", passwordFields.length);

document.addEventListener("submit",function(event)  {
     
        const form = event.target;
         const passwordField = form.querySelector('input[type="password"]');
         if (passwordField) {event.preventDefault(); 
                const answer = confirm( "Do you want  to save this password?"           
                );

                if (answer)
                         { console.log("User chose YES.");
                      const usernameField = form.querySelector(
                            ' input[type="email"], input[type="text"],  input[name="username"]' 
                          );

                        const username = usernameField?
                        usernameField.value: "";  
                        
                        const password = passwordField.value;
                        const website = window.location.hostname;


                        console.log("Website:", website);
                        console.log("Username:", username);
                        console.log("Password has been captured");

                chrome.runtime,sendMessage({
                        type:"SAVE_PASSWORD",
                        data: {
                                website: website,
                                username: username,
                                password: password
                        }
                });
             
                } else {console.log("User chose NO.");
               
                       
                     
                }
            
         }
       
        },true) ;
    