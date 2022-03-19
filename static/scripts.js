FORM_RULES = {
    '{{ form.title.name }}': 'required'
};
 
FORM_MESSAGES = {
    '{{ form.title.name }}': 'This field is required'
};
 
$(document).ready(function() {
    $('form').validate({
        rules: FORM_RULES,
        messages: FORM_MESSAGES
    });
});