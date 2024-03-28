document.addEventListener("DOMContentLoaded", function () {
    const validateBtn = document.getElementById("btnValidate")
    const checkDigitBtn = document.getElementById("btnCheckDigit")
    const resetBtn = document.getElementById("btnReset")
    const inputSequence = document.getElementById('sequence')
    const resultText = document.getElementById('result')

    let apiUrl = `http://127.0.0.1:5001`

    const validateSequence = async () => {
        const sequence = inputSequence?.value
        if (!sequence){
            alert("Input can't be empty")
        return
        }
        const response = await fetch(`${apiUrl}/check_is_valid?sequence=${sequence}`, {
            method: 'GET',
        })
        console.log(response)
        const responseJson = await response.json()
    
        if(response.status==200){
            const checkDigit = responseJson?.checkDigit
                const isValid = responseJson?.isValid
                resultText.style.visibility = 'visible'
                resultText.style.color = isValid ? 'green' : 'red'
                resultText.innerText = isValid ? `The sequence ${sequence} is valid` : `The sequence ${sequence} is In-Valid`
        }else {
            resultText.style.visibility = 'visible'
            resultText.style.color = 'red'
            resultText.innerText = responseJson?.error ? responseJson?.error:'Error in calling API !'
        }

    }

    const calculateCheckDigit = async () => {
        const sequence = inputSequence?.value
        if (!sequence){
            alert("Input can't be empty")
        return
        }
        const response = await fetch(`${apiUrl}/check_digit?sequence=${sequence}`, {
            method: 'GET',
        })
        
        const responseJson = await response.json()

        const checkDigit = responseJson?.checkDigit
        resultText.style.visibility = 'visible'
        resultText.innerText = `Check Digit for ${sequence} is ${checkDigit}`
    }

    const resetForm = () => {
        inputSequence.value = ''
        resultText.value = ''
        resultText.style.visibility = 'hidden'
    }

    validateBtn.addEventListener("click", validateSequence);
    checkDigitBtn.addEventListener("click", calculateCheckDigit);
    resetBtn.addEventListener("click", resetForm);
});
