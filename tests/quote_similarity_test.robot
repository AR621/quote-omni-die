*** settings ***
Documentation    General test case for checking similarity betweeen two quotes as to avoid duplicate or similar quotes
Library  ${CURDIR}${/}..\\scripts\\string_comparison.py
Library  ${CURDIR}${/}..\\scripts\\load_quotes.py

Suite Setup             load quotes for checking
Suite Teardown          none

*** test cases ***
Duplicate quote test
    [Documentation]    Fails if it finds duplicate quotes
    [Tags]  similarity check    duplicate check


    ${duplicate}=  Filter By Similarity         ${quotes}       tolerance=1.
    Should Be Empty         ${duplicate}
    [Teardown]  Run Keyword If Test Failed          log to console    $log as=ERROR    $variable to log=${duplicate}

quote similarity test
    [Documentation]    Fails if it finds too similar quotes, logs all the bad quotes as well as suspiciously similoar quotes
    [Tags]    similarity check

    ${similar}          Filter By Similarity    ${quotes}   tolerance=.50   upper_bound_ignore=.70
    ${very similar}     Filter By Similarity    ${quotes}   tolerance=.70   upper_bound_ignore=1.0

    IF  '@{similar}' != '@{EMPTY}'
    log to console    log as=WARN    variable to log=${similar}
    END

    [Teardown]  Run Keyword If Test Failed
    ...         log to console      log as=ERROR    variable to log=${very similar}

    Should Be Empty     ${very similar}

*** Keywords ***
load quotes for checking
    [Documentation]  loads quotes list from database and sets it as a suite variable
    ${quotes}=  Load Quotes  download=False  get_authors=False  get_quotes=True
    Set Suite Variable      ${quotes}

log to console
    [Documentation]     logs variable to console
    [Arguments]     ${log as}   ${variable to log}  ${message}=
    Run Keywords
    ...         Log     Found the following similar strings     ${log as}
    ...  AND    Log     quote ID 1 | quote ID 2 | similarity [0-1]
    ...  AND    Log     ${variable to log}                      ${log as}

