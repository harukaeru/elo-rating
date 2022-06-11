docker run -v ${PWD}:/client -v ${PWD}/../server:/server --rm openapitools/openapi-generator-cli generate -g typescript-axios -i /server/openapi-schema.yml -o /client/src/client-axios && echo '-------------'
echo $SERVER_PROTOCOL
echo $SERVER_HOST
sed -i '' "s/http:\/\/localhost/$SERVER_PROTOCOL:\/\/$SERVER_HOST/g" ./src/client-axios/base.ts

