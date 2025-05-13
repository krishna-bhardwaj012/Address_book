import { useState } from "react";

export default function AddressBook() {
  const [contacts, setContacts] = useState([]);
  const [form, setForm] = useState({ name: "", phone: "", address: "" });

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const addEntry = () => {
    if (form.name && form.phone && form.address) {
      setContacts([...contacts, form]);
      setForm({ name: "", phone: "", address: "" });
    }
  };

  const deleteEntry = (index) => {
    setContacts(contacts.filter((_, i) => i !== index));
  };

  const updateEntry = (index) => {
    setForm(contacts[index]);
    deleteEntry(index);
  };

  return (
    <div className="p-4 text-center">
      <h2 className="text-2xl font-bold">Address Book</h2>
      <input type="text" name="name" placeholder="Name" value={form.name} onChange={handleChange} className="border p-2 m-1" />
      <input type="text" name="phone" placeholder="Phone" value={form.phone} onChange={handleChange} className="border p-2 m-1" />
      <input type="text" name="address" placeholder="Address" value={form.address} onChange={handleChange} className="border p-2 m-1" />
      <button onClick={addEntry} className="bg-green-500 text-white p-2 m-1">Add</button>
      <ul>
        {contacts.map((contact, index) => (
          <li key={index} className="border p-2 my-1 flex justify-between">
            {contact.name} ({contact.phone}) - {contact.address}
            <div>
              <button onClick={() => updateEntry(index)} className="bg-yellow-500 text-white p-1 mx-1">Edit</button>
              <button onClick={() => deleteEntry(index)} className="bg-red-500 text-white p-1">Delete</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
