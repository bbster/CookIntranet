<template>
  <v-app id="form-login" class="primary">
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4 lg4>
            <v-card class="elevation-1 pa-3">
              <v-card-text>
                <div class="layout column align-center">
                  <h1 class="flex my-4 primary--text">{{title}}</h1>
                </div>
                <v-form>
                  <v-text-field append-icon="phone_iphone" name="login" label="핸드폰번호" type="text"
                                v-model="model.username" browser-autocomplete="off"></v-text-field>
                  <v-text-field append-icon="vpn_key" name="password" label="비밀번호" id="password" type="password"
                                v-model="model.password" browser-autocomplete="off"></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-btn icon>
                  <v-icon color="blue">fa fa-facebook-square fa-lg</v-icon>
                </v-btn>
                <v-btn icon>
                  <v-icon color="red">fa fa-google fa-lg</v-icon>
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn block color="primary" :loading="loading">Welcome</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
  </v-app>
</template>

<script>
  export default {
    layout: 'login',
    data: () => ({
      loading: false,
      model: {
        username: '',
        password: ''
      },
      title: '더쿡 관리자페이지'
    })
  }
</script>