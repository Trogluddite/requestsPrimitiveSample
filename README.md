# requestsPrimitiveSample 

This is a sample of an HTTP session with the Requests library
Its intended use is to demonstrate an authenticated session with a REST API 

I use this in an environment configured like this: 

1. Pyenv w/ Python >= 3.10
2. Requests library installed via pip 
3. Certifi library installed via pip 
4. CERT_PATH=`python -m certifi`
4. edit $CERT_PATH to add local CA certificate 
5. export SSL_CERT_FILE={$CERT_PATH}
6. export REQUESTS_CA_BUNDLE=${CERT_PATH}

I will also typically install iPython to allow interactive queries of the API.  


