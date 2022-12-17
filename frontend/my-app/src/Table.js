import React from 'react'
import './Table.css'
function Table() {
  return (
    <div className='container col-4 '>
        <table className="table table-striped">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">PDFs uploaded till date</th>
      <td>0</td>
    </tr>
    <tr>
      <th scope="row">PDFs decoded with QR code</th>
      <td>0</td>
    </tr>
    <tr>
      <th scope="row">PDFs without QR code</th>
      <td>0</td>
    </tr>
  </tbody>
</table>
    </div>
  )
}

export default Table