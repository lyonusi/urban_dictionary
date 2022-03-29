function run(input, parameters) {
	
	var app = Application.currentApplication()
	app.includeStandardAdditions = true
 
 	for (let i = 0; i < input.length; i++) { 
		var dialogText = input[i].replaceAll('[<>]', '\n')
		app.displayDialog(dialogText, {
    		buttons: ["OK, I get it", "Next"],
    		defaultButton: "Next",
    		cancelButton: "OK, I get it"
		})
	}
	return input;
}
