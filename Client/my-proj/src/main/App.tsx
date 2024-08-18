import './App.css'
import SimpleNav from './SimpleNav'
import Title from './Title'


const App = () => {
  // const [count, setCount] = useState(0)

  // fetchAPI for retrieving info from the backend
  

  return (
    <>
      <div className="border">
        <SimpleNav />
        <Title />
      </div>
    </>
  )
}

export default App

/* 
const fetchAPI = async () => {
    const response = await axios.get("http://localhost:5000/graph")
    console.log(response.data.graph);
  }

  useEffect(() => {
    fetchAPI();
  }, [])
*/