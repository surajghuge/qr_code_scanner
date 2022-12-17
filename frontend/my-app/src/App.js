import './App.css';
import Axiox from 'axios';
import { useState } from 'react';

function App() {

  let formdata = new FormData();
  const [data, setData] = useState([])
  const onFileChange = (e) => {
    console.log(e.target.files[0]);

    if (e.target && e.target.files[0]) {
      formdata.append('file_upload', e.target.files[0]);
    }
  }

  const submitFileData = () => {
    Axiox.post(
      'http://127.0.0.1:5000/upload/img', formdata
    ).then(res => {
      console.log(res.data);
      setData(res.data)
    }).catch(error => {
      console.log(error);
    })
  }

  return (
    <div className="App">
    <div className='container card mb-3 col-5'>
    <div className='container my-3'>
        <input type='file' className="form-control" name="file_upload" onChange={onFileChange} />
      </div>
      <div>
        <button className='submitBtn btn btn-primary' onClick={submitFileData}>Submit</button>
      </div>
    </div>
      

      <div className='container col-4'>
        <div className="card text-center">
          <div className="card-header">
            Decoded text
          </div>

          <div className="card-body">
            <ol className="card-text">
                {data.map((item,index)=>{
                    return <li key={index}>{item}</li>
                })}
            </ol>
          </div>
          <div className="card-footer text-muted">

          </div>
        </div>
      </div>

    </div>
  );
}

export default App;

