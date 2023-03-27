use pyo3::prelude::*;

/// This function is exported in Python as `mmocore.helloworld`.
#[pyfunction]
fn helloworld() -> PyResult<String> {
    Ok(("Hello, world!").to_string())
}

/// A Python module implemented in Rust.
#[pymodule]
fn core(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(helloworld, m)?)?;
    Ok(())
}
