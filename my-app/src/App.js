import './App.css';

function App() {
  return (
    <div className="App">
      <FormControl isRequired>
        <FormLabel>Total sum</FormLabel>
        <Input placeholder='Total' />
        <FormLabel>Share sum</FormLabel>
        <Input placeholder='Share_sum' />
        <FormLabel>Bank statement</FormLabel>
        <Input placeholder='Bank' />
        <Button
            mt={4}
            colorScheme='teal'
            isLoading={props.isSubmitting}
            type='submit'
          ></Button>
      </FormControl>  
    </div>
  );
}

export default App;
