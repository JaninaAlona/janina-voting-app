const { defineConfig } = require('@vue/cli-service')
console.log(process.env.VUE_APP_DEPLOY);
if (process.env.VUE_APP_DEPLOY === "prod") {
    module.exports = defineConfig({
        transpileDependencies: true,
    })
} else if (process.env.VUE_APP_DEPLOY === "dev") {
    module.exports = defineConfig({
        transpileDependencies: true,
        devServer: {
            allowedHosts: [
                process.env.VUE_APP_DOMAIN_URL,
            ],
        },
    })
}