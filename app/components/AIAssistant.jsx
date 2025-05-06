import React, { useState } from 'react';
import { View, StyleSheet, TextInput, ScrollView, ActivityIndicator } from 'react-native';
import { Button, Text, Surface } from 'react-native-paper';
import llmClient from '../utils/llmClient';

export default function AIAssistant() {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!input.trim()) return;
    
    setLoading(true);
    try {
      const result = await llmClient.query(input);
      if (result) {
        setResponse(result);
      }
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Surface style={styles.container}>
      <Text style={styles.title}>Virtual Assistant</Text>
      <Text style={styles.subtitle}>
        Hello! I am your digital marketing assistant. How can I help you today?
      </Text>
      
      <TextInput
        style={styles.input}
        multiline
        numberOfLines={4}
        value={input}
        onChangeText={setInput}
        placeholder="Type your question here..."
      />

      <Button
        mode="contained"
        onPress={handleSubmit}
        disabled={loading}
        style={styles.button}
      >
        {loading ? 'Processing...' : 'Submit'}
      </Button>

      {loading && <ActivityIndicator style={styles.loader} />}

      {response && (
        <ScrollView style={styles.responseContainer}>
          <Text style={styles.responseText}>{response}</Text>
        </ScrollView>
      )}
    </Surface>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 16,
    margin: 16,
    borderRadius: 8,
    elevation: 4,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 16,
    marginBottom: 16,
    color: '#666',
  },
  input: {
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 4,
    padding: 8,
    marginBottom: 16,
    minHeight: 100,
    textAlignVertical: 'top',
  },
  button: {
    marginBottom: 16,
  },
  loader: {
    marginVertical: 16,
  },
  responseContainer: {
    maxHeight: 200,
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 4,
    padding: 8,
  },
  responseText: {
    fontSize: 16,
    lineHeight: 24,
  },
});