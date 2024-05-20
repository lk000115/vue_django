import {reactive,onMounted} from 'vue'
import axios from 'axios'


export default function (){
    let dogList = reactive([])
      
    async function getDog(){

       try {
         let result = await axios.get('https://dog.ceo/api/breed/pembroke/images/random')
         dogList.push(result.data.message)
       } catch (error) {
         alert(error)
       }

    }
    return {dogList,getDog}

}