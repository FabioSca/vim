
# function ls_alias { wsl ls --color=auto -hF $args }
# Set-Alias -Name ls -Value ls_alias -Option AllScope

function ll_alias { ls --color=auto -hFl $args }
Set-Alias -Name ll -Value ll_alias -Option AllScope

# Set-PoshPrompt -Theme aliens

# Import the Chocolatey Profile that contains the necessary code to enable
# tab-completions to function for `choco`.
# Be aware that if you are missing these lines from your profile, tab completion
# for `choco` will not function.
# See https://ch0.co/tab-completion for details.
$ChocolateyProfile = "$env:ChocolateyInstall\helpers\chocolateyProfile.psm1"
if (Test-Path($ChocolateyProfile)) {
  Import-Module "$ChocolateyProfile"
}
