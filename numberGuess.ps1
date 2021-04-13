$maxValue = 10
$answer = 0

function playGame {
    $answer = generateNumber -maxValue $maxValue
    userGuess
}

function generateNumber {
    return Get-Random -Maximum $maxValue -Minimum 1
}

function userGuess {
    $userInput = Read-Host "Raad het getal tussen de 1 en de $($maxValue): "
    evaluateInput $userInput
}

function evaluateInput {
    try {
        $userInput = [int]$userInput
    } catch [System.Management.Automation.RuntimeException] {
        Write-Output "Voer aub. alleen een cijfer in!"
        userGuess
    }

    if ($userInput -gt 0 -and $userInput -le $maxValue) {
        if ($userInput -eq $answer) {
            Write-Output "*** GEFELICITEERD, $($userInput) IS HET JUISTE ANTWOORD! ***"
            break
        } else {
            giveHint($userInput)
        }
    } else {
        Write-Output "Alleen getallen tussen de 1 en de $($maxValue)!"
        userGuess
    }
}

function giveHint {
    if ($userInput -lt $answer) {
        Write-Output "Het getal wat je zoekt is groter!"
        userGuess
    }
    if ($userInput -gt $answer) {
        Write-Output "Het getal wat je zoekt is kleiner!"
        userGuess
    }
}
    

playGame
