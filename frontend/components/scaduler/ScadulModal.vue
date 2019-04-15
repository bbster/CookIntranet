<template>
  <v-layout row justify-center>
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on }">
        <v-btn v-on="on"
          class="scaduler_fab"
          fab
          small
          color="cyan accent-2"
          bottom
          right
          absolute
          @click="dialog = !dialog"
          >
          <v-icon>add</v-icon>
          </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">일정추가</span>
        </v-card-title>
        <v-card-text>
          <v-container grid-list-md>
            <v-layout wrap>
              <v-flex xs12 sm12 md12>
                <v-text-field label="date*" required></v-text-field>
              </v-flex>
              <v-flex xs12 sm12 md12>
                <v-text-field label="제목*" hint="제목" required></v-text-field>
              </v-flex>
              <v-flex xs12 sm12 md12>
                <v-textarea
                  label="일정상세*"
                  hint="일정상세"
                  persistent-hint
                  required
                ></v-textarea>
              </v-flex>
              <v-flex xs12>
                <v-text-field label="주소"></v-text-field>
              </v-flex>
              <v-flex xs12 sm6>
                <v-text-field label="전화" type="전화번호"></v-text-field>
              </v-flex>
              <v-flex xs12 sm6>
                <v-text-field label="대금" type="결제대금"></v-text-field>
              </v-flex>
              <v-flex xs12 sm6>
                <v-select
                  :items="['긴급', '메모', '배송']"
                  label="우선순위*"
                  required
                ></v-select>
              </v-flex>
              <!-- <v-flex xs12 sm6>
                <v-autocomplete
                  :items="['Skiing', 'Ice hockey', 'Soccer', 'Basketball', 'Hockey', 'Reading', 'Writing', 'Coding', 'Basejump']"
                  label="Interests"
                  multiple
                ></v-autocomplete>
              </v-flex> -->
            </v-layout>
          </v-container>
          <small>*표시는 필수 입력필드입니다</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" flat @click="dialog = false">취소</v-btn>
          <v-btn color="blue darken-1" flat @click="dialog = false">저장</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<script>
  export default {
    data: () => ({
      dialog: false
    })
  }
</script>